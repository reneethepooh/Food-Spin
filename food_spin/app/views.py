from django.shortcuts import render
from django.http import HttpResponseRedirect
from .EventForm import EventForm

def home(request):
	return render(request, '../templates/intro.html')

def spin(request):
	return render(request, '../templates/spin.html')

def result(request):
	return render(request, '../templates/result.html')

def signup(request):
	return render(request, '../templates/signup.html')

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