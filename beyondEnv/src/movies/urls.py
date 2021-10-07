from django.urls import path
from .views import MovieSelectFormView, AddMovieFormView

app_name='movies'


urlpatterns = [
	path('', MovieSelectFormView.as_view(), name='movie-select-view'),
	path('add/', AddMovieFormView.as_view(), name='add-movie-view'),
]