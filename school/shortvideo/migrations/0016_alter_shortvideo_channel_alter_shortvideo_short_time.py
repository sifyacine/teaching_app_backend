# Generated by Django 5.0.7 on 2024-08-08 23:12

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_channel_channel_img'),
        ('shortvideo', '0015_alter_shortvideo_channel_alter_shortvideo_short_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortvideo',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.channel'),
        ),
        migrations.AlterField(
            model_name='shortvideo',
            name='short_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 0, 12, 58, 534774)),
        ),
    ]