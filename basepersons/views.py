from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib import messages

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



def sitehomepage(request):
    return render(request, 'index.html')


# Create your views here.
def registerUser(request):
	form = UserCreationForm()
	if request.method == 'POST': #if someone has filled out a form do something.
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			user = authenticate(username=username, password=password) #authenticate user
			login(request, user)  #log user in
			messages.success(request, 'Registration Successful')
			return redirect('claim-creator')
		else:
			messages.success(request, 'Already Registered, please log in.')
	return render(request, 'user_registery.html', {'form': form} )



def loginPage(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('afterlogin')
	else:
		messages.error(request, "Please login to access this page.")
		return HttpResponseRedirect('index.html')


# Login User
def loginUser(request):
	if request.method == "POST":
		username = request.POST.get ('username' )
		password = request.POST.get ('password')
		user = authenticate(username = username, password = password)
		if user != None:
			login(request, user)
			return HttpResponseRedirect('afterlogin')
		else:
			messages.error(request, "Enter your data correctly.")
		return HttpResponseRedirect('site-home')




def createAccount(request):
    return render(request, 'create_account.html')





