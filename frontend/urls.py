from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import userPage_views
from . import post_views
from . import homePage_views
from . import comments_views

user_url_patterns = [
    path('', userPage_views.user_profile, name='user_profile'),
    path('edit/', userPage_views.edit, name="edit"),
    path('friends_list/', userPage_views.friends_list, name="friends_list"),
]

post_url_patterns = [
    #TODO: consider if URLS below belong to separate post_urls.py or move all URLs to one file
    path('createsocialpost/', post_views.create_social_post, name="create_social_post"),
    path('createtrainingpost/', post_views.create_training_post, name="create_training_post"),
    path('viewsocialpost/<post_id>/', post_views.view_social_post, name="view_social_post"),
    path('viewtrainingpost/<post_id>/', post_views.view_training_post, name="view_training_post"),
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

    #Comments endpoint
    path('training_comments/<int:post_id>/', comments_views.CreateListTrainingPostCommentsView.as_view(), name = 'training_post_comments'),

    #Home page REST endpoints
    path('home_page_users', homePage_views.ListRandomUsersView.as_view(), name = 'home_page_rnd_users'),
    path('home_page_posts', homePage_views.ListRandomPostsView.as_view(), name = 'home_page_rnd_posts'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

