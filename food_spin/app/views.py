from django.http import HttpResponseRedirect
from .EventForm import EventForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages


def home(request):
	return render(request, '../templates/intro.html')

def spin(request):
	user = request.user
	return render(request, '../templates/spin.html', {"user":user})

def result(request):
	return render(request, '../templates/result.html')

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('spin')
	template_name = '../templates/signup.html'

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				print(f"You are now logged in as {username}")
				return redirect('/spin')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "../templates/login.html", {"form":form})
				
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

#class Event(DetailView):
#    model = EventPkAndSlug
#    query_pk_and_slug = False