from django.urls import path, include
from .views import home_view, post_view_json

app_name = 'posts'


urlpatterns = [
    path('', home_view, name='home-view'),


    # endpoints
    path('posts-json/', post_view_json, name='post_view_json'),
]