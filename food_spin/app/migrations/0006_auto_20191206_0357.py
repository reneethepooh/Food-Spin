# Generated by Django 2.2.7 on 2019-12-06 03:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20191206_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='radius',
        ),
        migrations.AddField(
            model_name='event',
            name='followers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='EventSubmission',
        ),
    ]
