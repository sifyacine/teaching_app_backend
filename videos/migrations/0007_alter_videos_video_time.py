# Generated by Django 5.0.7 on 2024-09-06 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_alter_videos_video_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 6, 12, 44, 44, 393976)),
        ),
    ]