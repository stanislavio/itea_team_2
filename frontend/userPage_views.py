from django.shortcuts import render


def profile(request):
    return render(request, 'user_page.html')

def register_user(request):
    return render(request, 'register_user.html')

def login_user(request):
    return render(request, 'login_user.html')

def friends_posts(request):
    return render(request, 'friends_posts.html')

def profile_user(request):
    return render(request, 'profile_user.html')
    