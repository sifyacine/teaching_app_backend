# Generated by Django 5.0.7 on 2024-08-09 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 19, 50, 7, 965901)),
        ),
    ]