from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
	date_today = datetime.now().date()
	return render(request, 'main/home.html', {'date_today': date_today})


def login_view(request):
	error_message = None
	form = AuthenticationForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None and user.is_director==False:
			login(request, user)
			if request.GET.get('next'):
				return redirect(request.GET.get('next'))
			else:
				return redirect('home-view')
		else:
			error_message = 'Ops something went wrong. Please check you password is correct Or Are you sure you are a producer?'	

	return render(request, 'main/login.html', {'form': form, 'error_message': error_message})

def logout_view(request):
	logout(request)
	return redirect('login-view')