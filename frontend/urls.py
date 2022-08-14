from django.urls import path, include

from . import userPage_views
from . import post_views
from . import homePage_views

user_url_patterns = [
    path('', userPage_views.profile),
    path('register_user/', userPage_views.register_user, name="register_user"),
    path('login_user/', userPage_views.login_user, name="login_user"),
    path('friends_sposts/', userPage_views.friends_posts, name="friends_posts"),
    path('profile_user/', userPage_views.profile_user, name="profile_user"),
]


urlpatterns = [
    #Home page URL
    path('', homePage_views.index, name='index'),
    #User urls
    path('user/', include(user_url_patterns)),
    #TODO: consider if URLS below belong to separate post_urls.py or move all URLs to one file
    path('post/createpost/', post_views.create_post, name="create_post"),

]