# Generated by Django 2.2.7 on 2019-12-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restriction',
            name='user_id',
            field=models.BigIntegerField(db_index=True, default=99),
            preserve_default=False,
        ),
    ]
