from django.urls import path

from . import userPage_views
from . import post_views

urlpatterns = [
    path('', userPage_views.profile),
    path('register_user/', userPage_views.register_user, name="register_user"),
    path('login_user/', userPage_views.login_user, name="login_user"),
    path('friends_sposts/', userPage_views.friends_posts, name="friends_posts"),
    path('profile_user/', userPage_views.profile_user, name="profile_user"),
    #TODO: consider if URLS below belong to separate post_urls.py or move all URLs to one file
    path('createpost/', post_views.create_post, name="create_post"),
]