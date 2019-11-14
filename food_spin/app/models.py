from django.db import models

class UserProfile(models.Model):
	user = models.OneToOneField(User),
	profile_picture = models.ImageField(upload_to='thumbpath', blank=True),
	restrictions = models.ManyToManyField(Restriction)

class EventSubmission(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE),
	event = models.ForeignKey(Event, on_delete=models.CASCADE),
	location = models.CharField(max_length=30)
	preferences = models.ManyToManyField(Restriction)

class Event(models.Model):
	leader = models.ForeignKey(User, on_delete=models.CASCADE),
	followers = models.ManyToManyField(User),
	link = models.TextField(),
	status = models.CharField(max_length=15)

class Restriction(models.Model):
	name = models.CharField(max_length=20)
