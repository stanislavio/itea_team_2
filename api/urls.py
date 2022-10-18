from django.urls import path
from .views import UserListAPIView, RegistrationAPIView
from .home_page_api_views import ListRandomUsersView, ListRandomPostsView
from .comments_api_views import CreateListTrainingPostCommentsView

from .post_api_view import ListUserPostsView, CreateTrainingPost, GetAllTypesOfTrainingPost

 

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('user/', UserListAPIView.as_view(), name='current_user'),
    path('user/<user_id>', UserListAPIView.as_view(), name='account'),

    #Home page REST endpoints
    path('home_page_users/', ListRandomUsersView.as_view(), name = 'home_page_rnd_users'),
    path('home_page_posts/', ListRandomPostsView.as_view(), name = 'home_page_rnd_posts'),

    #Comments endpoint
    path('comments_api/<int:post_id>/', CreateListTrainingPostCommentsView.as_view(), name = 'post_comments'),

    path('userpostslist/', ListUserPostsView.as_view(), name="userposts"),

    path("training_posts/create/", CreateTrainingPost.as_view(), name="api_create_training_post"),
    #TODO: change reference to this in submit of the page

    path("training_posts/", GetAllTypesOfTrainingPost.as_view(), name="api_get_training_post"),
]