from django.db import models
from django_mysql.models import SetCharField, ListCharField

class UserProfile(models.Model):
	user = models.OneToOneField(User),
	restrictions = SetTextField(
		base_field=CharField(max_length=30)
	),
	spin_history = ListCharField(
		base_field=CharField(max_length=36),
		size=10,
		max_length=(36*10)
	),
	profile_picture = models.ImageField(upload_to='thumbpath', blank=True)
		
