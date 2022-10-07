from django.http import JsonResponse

from db.models import Comment, SocialPost, TrainingPost, User
from .serializers import CommentSerializer,  UserSerializer

from rest_framework.decorators import api_view
from rest_framework import serializers, generics, status, mixins

from rest_framework.generics import GenericAPIView

from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

class CreateListTrainingPostCommentsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = CommentSerializer

    authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.GET['post_type'])
        post_id = int(self.kwargs['post_id'])
        post = None
        if self.request.GET['post_type'] == 'social':
            post = SocialPost.objects.filter(id = post_id).first()
        else:
            post = TrainingPost.objects.filter(id = post_id).first()
        print("Number of comments:", post.comments.all().count())    
        post_comments = post.comments.all().prefetch_related('author')
        return post_comments
    #END def get_queryset(self):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        new_comment_ser = CommentSerializer(
            data = {
                'comment_text' : request.POST["comment_text"],
            }
        )

        new_comment = None
        if new_comment_ser.is_valid(raise_exception=False):
            new_comment = new_comment_ser.create(
                new_comment_ser.validated_data
            )
            new_comment.author = request.user
            new_comment.save()

        post_id = self.kwargs["post_id"]
        
        curr_post = None
        if request.POST['post_type'] == 'social':
            curr_post = SocialPost.objects.filter(id=post_id).first()
        else:
            curr_post = TrainingPost.objects.filter(id=post_id).first()
        curr_post.comments.add(new_comment)
        curr_post.save()

        comment_ser = CommentSerializer(new_comment)
        print(comment_ser.data)
        return JsonResponse(
            { 'comment': comment_ser.data }
        )
    #END def post(self, request, *args, **kwargs):