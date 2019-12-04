from django.shortcuts import render

def home(request):
	return render(request, '../templates/intro.html')

def spin(request):
	return render(request, '../templates/spin.html')

def result(request):
	return render(request, '../templates/result.html')

def signup(request):
	return render(request, '../templates/signup.html')

def pref(request):
	return render(request, '../templates/pref.html')