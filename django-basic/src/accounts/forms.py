from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import *

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=100, help_text='Enter Your First Name')
	Last_name = forms.CharField(max_length=100, help_text='Enter Your Last Name')
	email = forms.EmailField(help_text='Enter Valid Email Address (email@gmail.com)')
	

	class Meta:
		model = User
		fields = ['username', 'first_name', 'Last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bio']