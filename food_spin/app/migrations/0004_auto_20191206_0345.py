# Generated by Django 2.2.7 on 2019-12-06 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20191206_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='diet_restrictions',
        ),
        migrations.AddField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]