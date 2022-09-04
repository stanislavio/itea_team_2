from django.http import JsonResponse

from db.models import Comment, SocialPost, TrainingPost, User
from .serializers import CommentSerializer, ValidatingCommentSerializer, UserSerializer

from rest_framework.decorators import api_view
from rest_framework import serializers, generics, status, mixins

from rest_framework.generics import GenericAPIView

from rest_framework.response import Response


class CreateListTrainingPostCommentsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = CommentSerializer

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

        #This is not ideal, but the problem is:
        # I either can have a serializer, which validates external object (author), but will not serizliae nested objectes - that is will not provide authors, only IDs -CommentSerializer 
        # Output of validating serializer (ValidatingCommentSerializer):
                # {
                #     "id":104,
                #     "date_created":"2022-09-04T16:11:27.499011+03:00",
                #     "author":1,
                #     "comment_text":"2nd comment"
                # }

        # or I can have serializer, which will provide nested author objects in JSON, but will not validate nested relation - CommentSerializer
        #Output of non validating serializer (CommentSerializer). Note full author information pulled automatically (as I need it for frontend):
                # {
                #     "id":104,
                #     "date_created":"2022-09-04T16:11:27.499011+03:00",
                #     "author":"OrderedDict("[
                #         "(""id",
                #         1),
                #         "(""photo",
                #         "/media/media/kitty_.jpg"")",
                #         "(""username",
                #         "admin"")",
                #         "(""birthday",
                #         "None)",
                #         "(""email",
                #         "admin@local.host"")",
                #         "(""phone",
                #         "None)",
                #         "(""short_bio",
                #         "sadfasd asdfasd\r\n\r\nasdfasdfsad"")"
                #     ]")",
                #     "comment_text":"2nd comment"
                # }
        #So I made both just to see how to make validation work.
        
        new_comment_ser = ValidatingCommentSerializer(
            data = {
                'comment_text' : request.POST["comment_text"],
                'author' : request.user.id
            }
        )

        new_comment = None
        if new_comment_ser.is_valid(raise_exception=False):
            new_comment = new_comment_ser.create(
                new_comment_ser.validated_data
            )

        post_id = self.kwargs["post_id"]
        
        curr_post = None
        if request.POST['post_type'] == 'social':
            curr_post = SocialPost.objects.filter(id=post_id).first()
        else:
            curr_post = TrainingPost.objects.filter(id=post_id).first()
        curr_post.comments.add(new_comment)
        curr_post.save()

        new_comment_ser = ValidatingCommentSerializer(new_comment)
        comment_ser = CommentSerializer(new_comment)
        return JsonResponse(
            { 'comment': comment_ser.data }
        )
    #END def post(self, request, *args, **kwargs):