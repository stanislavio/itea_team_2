from django.http import JsonResponse

from db.models import Comment, SocialPost, TrainingPost, User
from .serializers import CommentSerializer, UserSerializer

from rest_framework.decorators import api_view
from rest_framework import serializers, generics, status, mixins

from rest_framework.generics import GenericAPIView

from rest_framework.response import Response


@api_view(['GET', 'POST'])
def comment_endpoint(request):
    print("Post_id received:")
    if request.method == "GET":
        print("Get:", request.GET)
        if "post_id" in request.GET:
            post_id = request.GET["post_id"]
            print("Have post ID:", post_id)

            post = SocialPost.objects.filter(id=post_id)[0]
            comments = post.comments.all()
            print("have comments:", comments)

            # comments = Comment.objects.filter()
            comment_ser = CommentSerializer(comments, many=True)

        return JsonResponse(
            {
                'comments': comment_ser.data,
            }
        )
    

    if request.method == "POST":
        print("Post method called")
        print(request.POST)

        new_comment = Comment(
            comment_text = request.POST["comment_text"],
            author = request.user)

        new_comment.save()

        curr_post = SocialPost.objects.filter(id=request.POST["post_id"])[0]
        print(curr_post.post_text)
        curr_post.comments.add(new_comment)
        curr_post.save()

        return Response('hello', status=status.HTTP_201_CREATED)
        


class CreateListTrainingPostCommentsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = int(self.kwargs['post_id'])
        training_post = TrainingPost.objects.filter(id = post_id)[0]
        post_comments = training_post.comments.all().prefetch_related('author')
        for comment in post_comments:
            print("Have author:", comment.author.username)
        return post_comments

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        new_comment = Comment(
            comment_text = request.POST["comment_text"],
            author = request.user
        )
        new_comment.save()

        curr_post = TrainingPost.objects.filter(id=self.kwargs["post_id"])[0]
        print(curr_post.post_text)
        curr_post.comments.add(new_comment)
        curr_post.save()
        return Response('hello', status=status.HTTP_201_CREATED)