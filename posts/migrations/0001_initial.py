# Generated by Django 5.0.7 on 2024-09-06 22:41

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.TextField(max_length=800)),
                ('post_likes', models.IntegerField(default=0)),
                ('post_comments', models.IntegerField(default=0)),
                ('post_time', models.DateTimeField(default=datetime.datetime(2024, 9, 6, 23, 41, 30, 562427, tzinfo=datetime.timezone.utc))),
                ('channel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.channel')),
            ],
        ),
        migrations.CreateModel(
            name='PostImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_images/%y/%m/%d')),
                ('postimage_time', models.DateTimeField(default=datetime.datetime(2024, 9, 6, 23, 41, 30, 563425, tzinfo=datetime.timezone.utc))),
                ('channel', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.channel')),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='posts.post')),
            ],
        ),
    ]