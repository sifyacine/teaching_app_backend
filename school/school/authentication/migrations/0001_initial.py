# Generated by Django 5.0.7 on 2024-08-02 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(default='Unknown', max_length=15)),
                ('channel_email', models.EmailField(default='example@gmail.com', max_length=254, unique=True)),
                ('channel_password', models.CharField(default='123456789', max_length=50)),
                ('channel_phone', models.CharField(default='0000000000', max_length=10, unique=True)),
                ('channel_img', models.ImageField(default='images/images.png', max_length=254, upload_to='channel_img/%y/%m/%d')),
                ('channel_type', models.CharField(default='student', max_length=9)),
                ('channel_desc', models.TextField(default='channel description', max_length=275)),
                ('channel_likes', models.IntegerField(default=0)),
                ('channel_aprove', models.BooleanField(default=False)),
                ('channel_verifycode', models.CharField(default=886359, max_length=6)),
                ('channel_createAT', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]