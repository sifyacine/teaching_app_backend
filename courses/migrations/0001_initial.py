# Generated by Django 5.0.7 on 2024-08-09 00:26

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_alter_channel_channel_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_title', models.CharField(max_length=100)),
                ('course_desc', models.TextField(max_length=800)),
                ('course_video_intro', models.FileField(upload_to='course/%y/%m/%d')),
                ('course_img_video', models.ImageField(upload_to='course/images/%y/%m/%d')),
                ('course_video_number', models.IntegerField()),
                ('course_rating', models.IntegerField()),
                ('course_time', models.DateTimeField(default=datetime.datetime(2024, 8, 9, 1, 26, 32, 240270))),
                ('channel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.channel')),
            ],
        ),
    ]