from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def home(request):
	return render(request, '../templates/intro.html')

def spin(request):
	return render(request, '../templates/spin.html')

def result(request):
	return render(request, '../templates/result.html')

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('spin')
	template_name = '../templates/signup.html'

def pref(request):
	return render(request, '../templates/pref.html')