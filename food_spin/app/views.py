from django.http import HttpResponseRedirect
from .EventForm import EventForm
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

# def pref(request):
# 	return render(request, '../templates/pref.html')

def create_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form=EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    return render(request, '../templates/createevent.html', {'form': form})