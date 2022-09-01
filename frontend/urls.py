from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import userPage_views
from . import post_views
from . import homePage_views

user_url_patterns = [
    path('', userPage_views.user_profile, name='user_profile'),
    path('edit/', userPage_views.edit, name="edit"),
    path('friends_list/', userPage_views.friends_list, name="friends_list"),
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
    path('post/createpost/', post_views.create_post, name="create_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)