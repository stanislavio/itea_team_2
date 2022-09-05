from django.urls import path
from .views import user_list
from .home_page_api_views import ListRandomUsersView, ListRandomPostsView
from .comments_api_views import CreateListTrainingPostCommentsView

urlpatterns = [
    path('user/', user_list),

    #Home page REST endpoints
    path('home_page_users/', ListRandomUsersView.as_view(), name = 'home_page_rnd_users'),
    path('home_page_posts/', ListRandomPostsView.as_view(), name = 'home_page_rnd_posts'),

    #Comments endpoint
    path('comments_api/<int:post_id>/', CreateListTrainingPostCommentsView.as_view(), name = 'post_comments'),

]