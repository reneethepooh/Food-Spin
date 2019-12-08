from django.http import HttpResponseRedirect
from .forms import EventForm, RestrictionForm, SubmissionForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from app.models import Restriction, Profile, Event, EventSubmission

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
		form = EventForm(request.POST)
		if form.is_valid():
			event_name = form.cleaned_data['event_name']
			location = form.cleaned_data['location']
			radius = form.cleaned_data['search_radius']
			new_event = Event.objects.create(name=event_name, location=location, radius=radius, host=request.user)
			new_submission = EventSubmission.objects.create(user=request.user, event=new_event)
			return redirect('submission', slug=new_event.slug)
		else:
			messages.error(request, 'Invalid event creation')
	else:
		form = EventForm()
	return render(request, '../templates/createevent.html', {'form':form})

def submit_event(request, slug):
	user = request.user
	event = Event.objects.get(slug=slug)
	url = request.get_full_path()

	try:
		submission = EventSubmission.objects.get(user=user, event=event)
	except EventSubmission.DoesNotExist:
		submission = EventSubmission.objects.create(user=user, event=event)

	if request.method == 'POST':
		if 'conclude' in request.POST:
			form = SubmissionForm(request.POST)
			event.status = 'Pending'
			return redirect ('results',slug=event.slug)
		else:
			form = SubmissionForm(request.POST)
			if form.is_valid():
				new_preference = Restriction.objects.create(name=form.cleaned_data.get('preference'))
				submission.preferences.add(new_preference)
	else:
		form = SubmissionForm()
	return render(request, '../templates/submission.html', {'url':url, 'user':user, 'form':form,'submission':submission,'event':event})

def profile_page(request):
	user = request.user
	profile = user.profile
	if request.method == 'POST':
		form = RestrictionForm(request.POST)
		if form.is_valid():
			new_preference = Restriction.objects.create(name=form.cleaned_data.get('restriction'))
			profile.restrictions.add(new_preference)
	else:
		form = RestrictionForm()
	return render(request, '../templates/profile.html', {'profile':profile,'form':form,'user':user})

def result_page(request,slug):
	event = Event.objects.get(slug=slug)
	print("Event----------")
	print(event.name)
	submissions=event.eventsubmission_set.all()
	print("Event Submission: ------")
	print(submission)
	# for preference in submission.preferences.all:
	# 	print(preference.name)
	


	# print(event_submissions)
	# event_preferences=[]
	# for submission in event_submissions.iterator():
	# 	print(submission.event.name)
	# 	for preference in submission.preferences.all:
	# 		event_preferences.append(preference.name)
	# print(event_preferences)




	# #display the result in the corresponding html page
	return render(request,'../templates/successpage.html')


	


def yelp_call(radius, location , preferences):
  yelpapi_key="jsF4Y56oGgdh4JFCZabwwDxxbOJtRJXWL7aI1GP90Gb36w49rxZLwAhoybma_hTqFZl1YXzmFyyY4-JE1XEm6T2r5eAjkoKG7L2U9ovk4tDgWs3Fmw1ty__KkBPLXXYx" 
  yelp_url="https://api.yelp.com/v3/businesses/search" 
  API_HOST = 'https://api.yelp.com' 
  SEARCH_PATH = '/v3/businesses/search'

  empty_pref=" "
  term = empty_pref.join(preferences)
  seearch_location = location
  SEARCH_LIMIT = 20
  search_radius=radius # search_radius in meters
  parameters={
  'term': term.replace(' ', '+'),
  'location': search_location.replace(' ', '+'),
  'limit': SEARCH_LIMIT,
  'radius':search_radius
  }
  
  url = '{0}{1}'.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))
  headers = {
    'Authorization': 'Bearer %s' % yelpapi_key,
  }
  response = requests.request('GET', url, headers=headers, params=parameters)
  restaurant_data=response.json()

  #Do data processing to define restaurant we get from API call
  return restaurant_data['businesses'][random.randint(0,19)]['name']