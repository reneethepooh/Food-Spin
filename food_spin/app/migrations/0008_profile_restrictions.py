# Generated by Django 2.2.7 on 2019-12-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_profile_restrictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='restrictions',
            field=models.ManyToManyField(to='app.Restriction'),
        ),
    ]
