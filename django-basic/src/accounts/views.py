from django.db.models.query_utils import PathInfo
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from requests.sessions import merge_setting
from getmac import get_mac_address
from django.contrib.auth import logout, login, authenticate
from .forms import *
from .models import *
import requests


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!. Now you are able to Login!.')
			return redirect('accounts:login')
	else:	
		form = UserRegisterForm()
	return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
	# print(request.user.first_name)
	# print(request.user.last_name)
	# print(request.user.email)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(
									request.POST,
									request.FILES,
									instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save() and p_form.save()
			messages.success(request, f'Youe Account has been Updated successfully! {request.user.username}')
			return redirect('accounts:bio')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
	}
	return render(request, 'accounts/profile.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def bio(request):
	return render(request, 'accounts/bio.html', {})

def login_view(request):
	loginusername = request.POST['lousername']
	loginpassword = request.POST['loginpass']

	user = authenticate(username=loginusername, password=loginpassword)

	if user is not None:
		login(request, user)
		return redirect('accounts:bio')
	return render(request, 'accounts/login.html', {})


def logout_view(request):
	logout(request)
	return redirect('accounts:login')
