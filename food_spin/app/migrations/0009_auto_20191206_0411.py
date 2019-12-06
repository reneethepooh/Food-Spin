# Generated by Django 2.2.7 on 2019-12-06 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0008_profile_restrictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default='Manhattan'),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.TextField(default='My Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='radius',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.TextField(default='Started'),
        ),
        migrations.AddField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='followers',
            field=models.ManyToManyField(related_name='participating', to=settings.AUTH_USER_MODEL),
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