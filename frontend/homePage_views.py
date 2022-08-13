from django.http import HttpResponse
from django.shortcuts import render

# from django import settings


def index(request):
    # return HttpResponse("This is home page, welcome")
    return render(request, 'home_page.html')