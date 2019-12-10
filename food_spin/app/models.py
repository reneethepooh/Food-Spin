from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.template.defaultfilters import slugify
import re

class Restriction(models.Model):
    name = models.CharField(max_length=20)
    user_id = models.BigIntegerField(db_index=True)

class Profile(models.Model):
	user_id = models.BigIntegerField(primary_key=True)
	restrictions = models.ManyToManyField(Restriction)

class Event(models.Model):
	name = models.TextField(default='My Event')
	user_id = models.BigIntegerField(db_index=True)
	status = models.TextField(default='Started')
	location = models.TextField(default='Manhattan')
	radius = models.IntegerField(default=10)
	slug = models.SlugField(max_length=50, unique=True, null=True)

	def save(self, **kwargs):
		slugfields = "%s-%s-%s" % (self.name, self.location, self.user_id)
		self.slug = slugify(slugfields)
		super(Event, self).save()

class EventSubmission(models.Model):
	user_id = models.BigIntegerField(db_index=True)
	event_id = models.BigIntegerField(db_index=True)
	preferences = models.ManyToManyField(Restriction)