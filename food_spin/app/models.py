from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Restriction(models.Model):
	name = models.CharField(max_length=20)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(owner=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwards):
	instance.profile.save()

class Profile(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
	restrictions = models.ManyToManyField(Restriction)

class Event(models.Model):
	name = models.TextField(default='My Event')
	host = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hosting', null=True)
	status = models.TextField(default='Started')
	location = models.TextField(default='Manhattan')
	radius = models.IntegerField(default=10)
	link = models.TextField(null=True)
	followers = models.ManyToManyField(User, related_name='participating')

class EventSubmission(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submission')
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='submissions')
	preferences = models.ManyToManyField(Restriction)