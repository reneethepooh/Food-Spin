from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.template.defaultfilters import slugify
import re


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
	host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosting', null=True)
	status = models.TextField(default='Started')
	location = models.TextField(default='Manhattan')
	radius = models.IntegerField(default=10)
	slug = models.SlugField(max_length=50, unique=True)

	def save(self, **kwargs):
		slug = "%s %s" % (self.name, self.location)
		unique_slugify(self, slug)
		super(Event, self).save()

class Restaurant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='restaurant') #related namee describes thee inverse relationship
    restaurant_name=models.TextField(default='')
    image_url=models.TextField(default='')
    yelp_url=models.TextField(default='')
    address=models.TextField(default='')


class EventSubmission(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submission')
	event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='submissions')
	preferences = models.ManyToManyField(Restriction, related_name='submission')

# The following two functions unique_slugify() and _slug_strip where taken from online
# https://djangosnippets.org/snippets/690/ and are used for slug generation in Events
# This code was not written by any group member
def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    """
    Calculates and stores a unique slug of ``value`` for an instance.

    ``slug_field_name`` should be a string matching the name of the field to
    store the slug in (and the field to check against for uniqueness).

    ``queryset`` usually doesn't need to be explicitly provided - it'll default
    to using the ``.all()`` queryset from the model's default manager.
    """
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    # Sort out the initial slug, limiting its length if necessary.
    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    # Create the queryset if one wasn't explicitly provided and exclude the
    # current instance from the queryset.
    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    # Find a unique slug. If one matches, at '-2' to the end and try again
    # (then '-3', etc).
    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    """
    Cleans up a slug by removing slug separator characters that occur at the
    beginning or end of a slug.

    If an alternate separator is used, it will also replace any instances of
    the default '-' separator with the new separator.
    """
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    # Remove multiple instances and if an alternate separator is provided,
    # replace the default '-' separator.
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    # Remove separator from the beginning and end of the slug.
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value