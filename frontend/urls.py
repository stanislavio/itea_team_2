from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import userPage_views, post_views, homePage_views
from . import comments_views

user_url_patterns = [
    path('', userPage_views.user_profile, name='user_profile'),
    path('<pk>', userPage_views.user_profile, name='user_profile_with_pk'),
    path('change_friend_status/<operation>/<pk>', userPage_views.change_friend_status, name='change_friend_status'),
    path('edit/', userPage_views.edit, name="edit"),
    path('friends_list/', userPage_views.friends_list, name="friends_list"),
    # path('send_friend_request/<int:user_id>/', userPage_views.send_friend_request, name='send_friend_request'),
    # path('accept_friend_request/<int:request_id>/', userPage_views.accept_friend_request, name='accept_friend_request'),
]

post_url_patterns = [
    #TODO: consider if URLS below belong to separate post_urls.py or move all URLs to one file
    path('socialpost/', post_views.create_social_post, name="create_social_post"),
    path('trainingpost/', post_views.create_training_post, name="create_training_post"),
    path('socialpost/<post_id>/', post_views.view_social_post, name="view_social_post"),
    path('trainingpost/<post_id>/', post_views.view_training_post, name="view_training_post"),
]


urlpatterns = [
    #Home page URL
    path('', homePage_views.index, name='index'),
    path('register_user/', homePage_views.register_user, name="register_user"),
    path('login_user/', homePage_views.login_user, name="login_user"),
    path('logout_user/', homePage_views.logout_user, name="logout_user"),
    #User urls
    path('user/', include(user_url_patterns)),
    #Post urls
    path('post/', include(post_url_patterns)),

    
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

