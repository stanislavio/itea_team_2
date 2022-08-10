from django.shortcuts import render


def profile(request):
    return render(request, 'user_page.html')