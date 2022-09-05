from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import CreateUserForm
from db.models import User, SocialPost

from django.contrib.auth import authenticate, login, logout



def index(request):
    context ={}
    return render(request, 'home_page.html', context)

def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
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
    logout(request)
    return redirect("login_user")

def login_user(request):
    if request.method == "POST":
        usr_name = request.POST.get('username')
        usr_pass = request.POST.get('password')
        
        user = authenticate(request, username=usr_name, password = usr_pass)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.success(request, "Username or password is not correct.")
    context ={}
    context["no_login_link"] = True
    return render(request, 'login_user.html', context)



