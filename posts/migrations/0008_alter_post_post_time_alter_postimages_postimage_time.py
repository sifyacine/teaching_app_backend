# Generated by Django 5.0.7 on 2024-09-07 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_post_time_alter_postimages_postimage_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 23, 37, 5, 147210, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='postimages',
            name='postimage_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 23, 37, 5, 148210, tzinfo=datetime.timezone.utc)),
        ),
    ]
