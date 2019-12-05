from django.db import models
from django.contrib.auth.models import User

class Restriction(models.Model):
	name = models.CharField(max_length=20)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE),
	profile_picture = models.ImageField(upload_to='thumbpath', blank=True),
	restrictions = models.ManyToManyField(Restriction)

class Event(models.Model):
	leader = models.ForeignKey(User, on_delete=models.CASCADE),
	followers = models.ManyToManyField(User),
	link = models.TextField(),
	status = models.CharField(max_length=15),
	location = models.CharField(max_length=30),
	radius = models.IntegerField()

class EventSubmission(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE),
	event = models.ForeignKey(Event, on_delete=models.CASCADE),
	preferences = models.ManyToManyField(Restriction)
