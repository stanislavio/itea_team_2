from django.urls import path, include

from . import userPage_views
from . import post_views
from . import homePage_views

user_url_patterns = [
    path('', userPage_views.profile),
    
    path('friends_sposts/', userPage_views.friends_posts, name="friends_posts"),
    path('profile_user/', userPage_views.profile_user, name="profile_user"),
]


urlpatterns = [
    #Home page URL
    path('', homePage_views.index, name='index'),
    path('register_user/', homePage_views.register_user, name="register_user"),
    path('login_user/', homePage_views.login_user, name="login_user"),
    path('logout_user/', homePage_views.logout_user, name="logout_user"),
    #User urls
    path('user/', include(user_url_patterns)),
    #TODO: consider if URLS below belong to separate post_urls.py or move all URLs to one file
    path('post/createsocialpost/', post_views.create_social_post, name="create_social_post"),
    path('post/createtrainingpost/', post_views.create_training_post, name="create_training_post"),
    path('post/viewsocialpost/<post_id>/', post_views.view_social_post, name="view_social_post"),
    path('post/viewtrainingpost/<post_id>/', post_views.view_training_post, name="view_training_post"),

]