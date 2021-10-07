from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name='accounts'

# give redirect or Url to any page Like = ('accounts:login')

urlpatterns = [
    # path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('login/', login_view, name="login"),
    path('register', register, name='register'),
    path('profile/', profile, name='profile'),
    path('', bio, name='bio'),
    path('logout', logout_view, name='logout')
]