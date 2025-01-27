# Generated by Django 5.0.7 on 2024-08-08 22:32

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_channel_channel_img'),
        ('shortvideo', '0007_alter_shortvideo_short_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortvideo',
            name='channel',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.channel'),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='short_comments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='short_likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='short_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 8, 23, 32, 49, 443917)),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='short_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='short_video',
            field=models.FileField(blank=True, null=True, upload_to='shortvideo/%y/%m/%d'),
        ),
    ]
