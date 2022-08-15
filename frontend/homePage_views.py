from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateUserForm

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
    return render(request, 'login_user.html')