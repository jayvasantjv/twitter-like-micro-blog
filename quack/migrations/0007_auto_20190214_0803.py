# Generated by Django 2.1.5 on 2019-02-14 08:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quack', '0006_auto_20190214_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2019, 2, 14, 8, 3, 8, 51768, tzinfo=utc)),
        ),
    ]
