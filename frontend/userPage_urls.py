from django.urls import path

from . import userPage_views

urlpatterns = [
    path('', userPage_views.profile)
]