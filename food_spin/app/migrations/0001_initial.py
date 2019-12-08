# Generated by Django 2.2.7 on 2019-12-07 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='My Event')),
                ('status', models.TextField(default='Started')),
                ('location', models.TextField(default='Manhattan')),
                ('radius', models.IntegerField(default=10)),
                ('link', models.SlugField(unique=True)),
                ('followers', models.ManyToManyField(related_name='participating', to=settings.AUTH_USER_MODEL)),
                ('host', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosting', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('restrictions', models.ManyToManyField(to='app.Restriction')),
            ],
        ),
        migrations.CreateModel(
            name='EventSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='app.Event')),
                ('preferences', models.ManyToManyField(to='app.Restriction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
