# Generated by Django 5.0.7 on 2024-09-06 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_alter_videos_video_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 6, 23, 36, 31, 852351)),
        ),
    ]
