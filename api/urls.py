from django.urls import path
from .views import user_list
from .home_page_api_views import ListRandomUsersView, ListRandomPostsView

urlpatterns = [
    path('user/', user_list),

    #Home page REST endpoints
    path('home_page_users/', ListRandomUsersView.as_view(), name = 'home_page_rnd_users'),
    path('home_page_posts/', ListRandomPostsView.as_view(), name = 'home_page_rnd_posts'),
]