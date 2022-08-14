from django.http import HttpResponse
from django.shortcuts import render

# from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def index(request):
    # return HttpResponse("This is home page, welcome")
    return render(request, 'home_page.html')

def register_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
    context = {'form' : form}
    return render(request, 'register_user.html', context)

def login_user(request):
    return render(request, 'login_user.html')