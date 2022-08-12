from django.urls import path

from . import userPage_views

urlpatterns = [
    path('', userPage_views.profile),
    path('test_base/', userPage_views.test_base)
]