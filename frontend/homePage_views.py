from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import CreateUserForm
from db.models import User

from django.contrib.auth import authenticate, login, logout

from .serializers import UserSerializer
from rest_framework import serializers, generics, status, mixins
from rest_framework.generics import GenericAPIView

import random

def index(request):
    context ={}
    return render(request, 'home_page.html', context)

def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
    context = {
        'form' : form,
        'no_register_link' : True,
    }
    return render(request, 'register_user.html', context)

def logout_user(request):
    print("Logging out user")
    logout(request)
    return redirect("login_user")

def login_user(request):
    if request.method == "POST":
        usr_name = request.POST.get('username')
        usr_pass = request.POST.get('password')
        
        user = authenticate(request, username=usr_name, password = usr_pass)

        if user is not None:
            login(request, user)
            print("Success")
            return redirect("index")
        else:
            print("Not authenticated")
            messages.success(request, "Username or password is not correct.")
    context ={}
    context["no_login_link"] = True
    return render(request, 'login_user.html', context)



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