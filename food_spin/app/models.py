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
	host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosting', null=True, blank=True)
	status = models.TextField(default='Started')
	location = models.TextField(default='Manhattan')
	radius = models.IntegerField(default=10)
	link = models.TextField(null=True)
	followers = models.ManyToManyField(User, related_name='participating')

class EventSubmission(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submission')
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='submissions')
	preferences = models.ManyToManyField(Restriction)

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