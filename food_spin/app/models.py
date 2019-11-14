from django.db import models
from django_mysql.models import SetCharField,

class UserProfile(models.Model):
	user = models.OneToOneField(User),
	restrictions = SetTextField(
		base_field=CharField(max_length=30)
	),
	profile_picture = models.ImageField(upload_to='thumbpath', blank=True),
	friends = models.ManyToManyField(User)

class EventSubmission(models.Model):
	user = models.OneToOneField(UserProfile),
	event = models.OneToOneField(Event),
	preferences = SetTextField(
		base_field=CharField(max_length=30)
	),
	location = models.CharField(max_length=30)

class Event(models.Model):
	leader = models.OneToOneField(User),
	followers = models.ManyToManyField(User),
	submissions = models.ManyToManyField(EventSubmission),
	link = models.TextField(),
	status = models.CharField(max_length=15) 
