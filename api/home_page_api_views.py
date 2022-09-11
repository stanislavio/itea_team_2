from .serializers import UserSerializer, SocialPostSerializer
from rest_framework import serializers, generics, status, mixins
from rest_framework.generics import GenericAPIView

from db.models import Comment, User, SocialPost, TrainingPost

import random

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer, SocialPostSerializer, TrainingPostSerializer



def getRandomObjects(modelManager, number_needed):
    #this relies that identity field is id, will not work with other keys
    number_of_objects = modelManager.all().count()
    print('number_of_objects', number_of_objects)
    objects_list = modelManager.all()

    rnd_object_no = random.randint(0, number_of_objects-1)

    id_set = {objects_list[rnd_object_no].id}

    object_list_union = modelManager.filter(
        id = objects_list[rnd_object_no].id
    )

    if number_of_objects < number_needed:
        return objects_list
    
    for i in range(number_needed-1):
        rnd_object_no = random.randint(0, number_of_objects-1)
        curr_object_id = objects_list[rnd_object_no].id
        while curr_object_id in id_set:
            rnd_object_no = random.randint(0, number_of_objects-1)
            curr_object_id = objects_list[rnd_object_no].id
        id_set.add(objects_list[rnd_object_no].id)

        object_list_union = object_list_union.union(
            modelManager.filter(
                id = curr_object_id
            )
        )#object_list_union.union(
        # print("COunt of objects:", object_list_union.count())

    return object_list_union
#def getRandomObjects(modelManager, number_needed):


class ListRandomUsersView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = UserSerializer
    NO_OF_USERS_TO_RETURN = 6

    def get_queryset(self):
        user_list_union = getRandomObjects(User.objects, self.NO_OF_USERS_TO_RETURN)
        return user_list_union

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class ListRandomPostsView(APIView):

    NO_OF_POSTS_TO_RETURN = 4

    def get(self, request, format=None):

        soc_post_queryset = getRandomObjects(SocialPost.objects, self.NO_OF_POSTS_TO_RETURN)

        train_post_queryset = getRandomObjects(TrainingPost.objects, self.NO_OF_POSTS_TO_RETURN)


        
        social_posts_list = list(soc_post_queryset)
                
        training_posts_list = list(train_post_queryset)

        combined_list = training_posts_list+social_posts_list

        combined_list.sort(
                    key=lambda elem: elem.date_created,
                    reverse=True
        )

        combinedJSON = [
            #List comprehension with ternary operator 
            SocialPostSerializer(post).data 
                    if type(post) == SocialPost 
                    else TrainingPostSerializer(post).data
            for post in combined_list
        ]

        # for post in combined_list:
        #     if type(post) == SocialPost:
        #         combinedJSON.append(SocialPostSerializer(post).data)
        #     else:
        #         combinedJSON.append(TrainingPostSerializer(post).data)

        # training_posts_list_ser = TrainingPostSerializer(training_posts_list, many=True)
        return Response(combinedJSON)



# class ListRandomPostsView(mixins.ListModelMixin, GenericAPIView):
#     #TODO add training posts to home page
#     serializer_class = SocialPostSerializer
#     NO_OF_POSTS_TO_RETURN = 6

#     def get_queryset(self):
#         post_list = getRandomObjects(SocialPost.objects, self.NO_OF_POSTS_TO_RETURN)
#         return post_list

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)