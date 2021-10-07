from django.contrib import admin
from .models import Movie, Film, Commercial
from actors.models import Actor

class FilmModeAdmin(admin.ModelAdmin):
	def render_change_form(self, request, context, *args, **kwargs):
		context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(is_star=True)
		return super().render_change_form(request, context, *args, **kwargs)

class CommercialModeAdmin(admin.ModelAdmin):
	def render_change_form(self, request, context, *args, **kwargs):
		context['adminform'].form.fields['actors'].queryset = Actor.objects.filter(is_star=False)
		return super().render_change_form(request, context, *args, **kwargs)		


admin.site.register(Film, FilmModeAdmin)
admin.site.register(Commercial, CommercialModeAdmin)