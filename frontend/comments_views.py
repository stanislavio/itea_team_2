from django.http import JsonResponse

from db.models import Comment, SocialPost
from .serializers import CommentSerializer

from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status

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
        
        # JsonResponse(
        #     {
        #         'test_responce': [],
        #     }
        # )
        # comment_ser = CommentSerializer(data = request.data)
        # if comment_ser.is_valid():
        #     comment_ser.save()