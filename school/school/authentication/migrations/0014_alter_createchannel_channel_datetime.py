# Generated by Django 5.0.7 on 2024-08-03 23:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_rename_email_checkemail_channel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createchannel',
            name='channel_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 4, 0, 19, 35, 993127)),
        ),
    ]
