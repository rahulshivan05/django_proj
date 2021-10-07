from django.contrib import admin
from django.urls import path, include
from .views import home_view, login_view, logout_view

admin.site.site_header = 'Movies Administration'
admin.site.index_title = 'Manage the movies site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('login/', login_view, name='login-view'),
    path('logout/', logout_view, name='logout-view'),
    path('movies/', include('movies.urls', namespace='movies')),
    path('users/', include('users.urls', namespace='users')),
]
