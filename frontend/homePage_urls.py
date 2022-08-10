from django.urls import path

from . import homePage_views

urlpatterns = [
    path('', homePage_views.index, name='index'),
]