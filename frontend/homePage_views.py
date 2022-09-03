from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import CreateUserForm
from db.models import User

from django.contrib.auth import authenticate, login, logout

from .serializers import UserSerializer
from rest_framework import serializers, generics, status, mixins
from rest_framework.generics import GenericAPIView

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


class ListRandomUsersView(mixins.ListModelMixin, GenericAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        number_of_users = User.objects.all().count()
        users_list = User.objects.all()[:number_of_users-1]
        return users_list

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)