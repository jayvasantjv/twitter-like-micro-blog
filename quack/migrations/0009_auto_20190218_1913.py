# Generated by Django 2.1.5 on 2019-02-18 19:13

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quack', '0008_auto_20190218_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2019, 2, 18, 19, 13, 8, 328654)),
        ),
        migrations.AlterField(
            model_name='quack',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='fans', to=settings.AUTH_USER_MODEL),
        ),
    ]
