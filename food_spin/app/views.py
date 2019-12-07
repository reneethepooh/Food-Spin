from django.http import HttpResponseRedirect
from .forms import EventForm, PrefForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from app.models import Restriction, Profile

def home(request):
	return render(request, '../templates/intro.html')

def spin(request):
	user = request.user
	return render(request, '../templates/spin.html', {'user':user})

def result(request):
	return render(request, '../templates/result.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/spin')
		else:
			messages.error(request, 'Invalid username or password.')
	form = UserCreationForm()
	return render(request, '../templates/signup.html', {'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect('login')

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/spin')
			else:
				messages.error(request, 'Invalid username or password.')
		else:
			messages.error(request, 'Invalid username or password.')
	form = AuthenticationForm()
	return render(request, '../templates/login.html', {'form':form})
				
def create_event(request):
	if request.method == 'POST':
		if form.is_valid():
			valid_form=form.cleaned_data
			new_event=valid_form.save()
			return HttpResponseRedirect('spin')
		else:
			form=EventForm()
	else:#when there is a get request
		form=EventForm()
		
	args = {'form': form}
	return render(request, '../templates/createevent.html',args)

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = EventForm()

    # return render(request, '../templates/createevent.html', {'form': form})

#class Event(DetailView):
#    model = EventPkAndSlug
#    query_pk_and_slug = False

def profile_page(request):
	user = request.user
	profile = user.profile
	if request.method == 'POST':
		form=PrefForm(request.POST)
		if form.is_valid():
			new_preference = Restriction.objects.create(name=form.cleaned_data.get('new_pref'))
			profile.restrictions.add(new_preference)
	else:
		form = PrefForm()
	return render(request, '../templates/profile.html', {'profile':profile, 'form':form, 'user':user})