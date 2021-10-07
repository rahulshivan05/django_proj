from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import Film, Commercial
from .forms import MovieSelectForm, FilmModelForm, CommercialModelForm
from django.contrib.auth.mixins import LoginRequiredMixin

class MovieSelectFormView(LoginRequiredMixin, FormView):
	form_class = MovieSelectForm
	template_name = 'movies/main.html'
	success_url = reverse_lazy('movies:add-movie-view')

	def post(self, *args, **kwargs):
		self.request.session['movie'] = self.request.POST.get('movie').lower().capitalize()
		print(self.request.POST.get('movie').lower().capitalize())
		return super().post(*args, **kwargs)


class AddMovieFormView(LoginRequiredMixin, FormView):
	template_name = 'movies/add.html'
	success_url = reverse_lazy('home-view')

	def get_form_class(self, *args, **kwargs):
		movie = self.request.session.get('movie')
		if movie == 'Commercial':
			return CommercialModelForm
		else:
			return FilmModelForm

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)



