import itertools
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Restriction(models.Model):
	name = models.CharField(max_length=20)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE),
	profile_picture = models.ImageField(upload_to='thumbpath', blank=True),
	restrictions = models.ManyToManyField(Restriction)

class Event(models.Model):
	name = models.CharField(max_length=30),
	leader = models.ForeignKey(User, on_delete=models.CASCADE),
	followers = models.ManyToManyField(User),
	link = models.TextField(),
	status = models.CharField(max_length=15),
	location = models.CharField(max_length=30),
	radius = models.IntegerField()

class EventUniqueSlug(Event):
	slug = models.SlugField(default='', max_length=250, null=True, blank=True)

	def get_absolute_url(self):
		kwargs = {"slug": self.slug}
		return reverse("eventunique-slug", kwargs=kwargs)

	def _generate_slug(self):
		max_length = self._meta.get_field("slug").max_length
		#slug = slugify(self.name)[:max_length]
		value = self.name
		slug_candidate = slug_original =  slugify(value, allow_unicode=True)
		for i in itertools.count(1):
			if not EventUniqueSlug.objects.filter(slug=slug_candidate).exists():
				break
			slug_candidate = "{}-{}".format(slug_original, i)

		self.slug = slug_candidate

	def save(self, *args, **kwargs):
		if not self.pk:
			self._generate_slug()

		super().save(*args, **kwargs)

'''
class EventPkAndSlug(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(
		default="", editable=False, max_length=250
	)

	def get_absolute_url(self):
		kwargs =  {"pk": self.id, "slug": self.slug}
		return reverse("event-pk-slug-detail", kwargs=kwargs)

	def save(self, *args, **kwargs):
		value = self.name
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs) 
'''


class EventSubmission(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE),
	event = models.ForeignKey(Event, on_delete=models.CASCADE),
	preferences = models.ManyToManyField(Restriction)
