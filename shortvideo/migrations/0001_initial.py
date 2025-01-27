# Generated by Django 5.0.7 on 2024-08-07 23:11

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
            name='ShortVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_title', models.CharField(max_length=100)),
                ('short_video', models.FileField(upload_to='shortvideo/%y/%m/%d')),
                ('short_likes', models.IntegerField()),
                ('short_comments', models.IntegerField()),
                ('short_time', models.DateTimeField(default=datetime.datetime(2024, 8, 8, 0, 11, 36, 218119))),
                ('channel_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.channel')),
            ],
        ),
    ]
