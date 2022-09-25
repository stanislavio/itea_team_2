from .serializers import UserSerializer, SocialPostSerializer, TrainingPostSerializer
from rest_framework import serializers, generics, status, mixins
from rest_framework.generics import GenericAPIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from db.models import SocialPost, TrainingPost, RunTrainingPost, HikeTrainingPost, SwimTrainingPost


from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from datetime import datetime

class CreateTrainingPost(APIView):
    def post(self, request, *args, **kwargs):
        print("Create training topic called")
        print(request.POST)

        dt_started = datetime.fromisoformat(request.POST["datetime_started"][:-1])
        dt_finished = None
        if len(request.POST["datetime_finished"])>0:
            dt_finished = datetime.fromisoformat(request.POST["datetime_finished"][:-1])

        post_private = True if request.POST["post_is_private"] == "true" else False

        new_post = None

        if request.POST["post_type"] == "running":
            print("Creating running post")
            print(request.POST["datetime_started"])
            new_post = RunTrainingPost(
                post_title = request.POST["post_title"],
                post_text = request.POST["post_text"], 
                datetime_started = dt_started,
                datetime_finished = dt_finished,    
                post_is_private = post_private,
                author = request.user,
                total_km_ran = request.POST["total_km_ran"]
            )

            new_post.save()

            print("Post is private", request.POST["post_is_private"])
        #END if request.POST["post_type"] == "running":

        if request.POST["post_type"] == "hiking":
            print("Creating hiking post")
            # print(request.POST["datetime_started"])
            new_post = HikeTrainingPost(
                post_title = request.POST["post_title"],
                post_text = request.POST["post_text"], 
                datetime_started = dt_started,
                datetime_finished = dt_finished,    
                post_is_private = post_private,
                author = request.user,
                total_km_walked = request.POST["total_km_walked"],
                hike_location = request.POST["hike_location"],
                max_elevation = request.POST["max_elevation"]
            )
            new_post.save()
            # print("Post is private", request.POST["post_is_private"])
        #END if request.POST["post_type"] == "hiking":

        if request.POST["post_type"] == "swimming":
            print("Creating swimming post")
            new_post = SwimTrainingPost(
                post_title = request.POST["post_title"],
                post_text = request.POST["post_text"], 
                datetime_started = dt_started,
                datetime_finished = dt_finished,    
                post_is_private = post_private,
                author = request.user,
                total_km_swum = request.POST["total_km_swum"],
                swimming_location = request.POST["swimming_location"]   
            )
            new_post.save()
            # print("Post is private", request.POST["post_is_private"])
        #END if request.POST["post_type"] == "swimming":


        return JsonResponse(
            { 'result': "OK" }
        )





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
#END class ListUserPostsView(APIView):

