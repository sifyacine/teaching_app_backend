# Generated by Django 5.0.7 on 2024-08-03 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_createchannel_channel_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createchannel',
            name='channel_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 3, 23, 44, 49, 314588)),
        ),
    ]