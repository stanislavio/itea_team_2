from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

def index(request):

    return render(request, 'home_page.html')

def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_user")
    context = {'form' : form}
    return render(request, 'register_user.html', context)

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
            messages.info(request, "Username or password is not correct.")
    context ={}
    return render(request, 'login_user.html', context)