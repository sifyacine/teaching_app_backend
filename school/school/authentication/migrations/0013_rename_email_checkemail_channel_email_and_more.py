# Generated by Django 5.0.7 on 2024-08-03 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_checkemail_alter_createchannel_channel_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkemail',
            old_name='email',
            new_name='channel_email',
        ),
        migrations.AlterField(
            model_name='createchannel',
            name='channel_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 4, 0, 13, 13, 122202)),
        ),
    ]
