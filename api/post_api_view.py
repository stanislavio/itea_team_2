from .serializers import UserSerializer, SocialPostSerializer, TrainingPostSerializer
from rest_framework import serializers, generics, status, mixins
from rest_framework.generics import GenericAPIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from db.models import SocialPost, TrainingPost


from rest_framework.views import APIView
from rest_framework.response import Response

class ListUserPostsView(APIView):

    def get(self, request, format=None):

        social_posts = SocialPost.objects.filter(author=self.request.user.id)
        social_posts_list = list(social_posts)
        
        training_posts = TrainingPost.objects.filter(author=self.request.user.id)
        training_posts_list = list(training_posts)

        combined_list = training_posts_list+social_posts_list

        combined_list.sort(
                    key=lambda elem: elem.date_created,
                    reverse=True
        )

        combinedJSON = []

        for post in combined_list:
            if type(post) == SocialPost:
                combinedJSON.append(SocialPostSerializer(post).data)
            else:
                combinedJSON.append(TrainingPostSerializer(post).data)

        return Response(combinedJSON)

