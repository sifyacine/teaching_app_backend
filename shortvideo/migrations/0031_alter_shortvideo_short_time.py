# Generated by Django 5.0.7 on 2024-09-07 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortvideo', '0030_alter_shortvideo_short_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortvideo',
            name='short_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 23, 18, 59, 725198)),
        ),
    ]