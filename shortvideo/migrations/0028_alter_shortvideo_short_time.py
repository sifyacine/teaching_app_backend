# Generated by Django 5.0.7 on 2024-09-06 22:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortvideo', '0027_alter_shortvideo_short_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortvideo',
            name='short_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 6, 23, 58, 29, 605742)),
        ),
    ]
