# Generated by Django 5.0.7 on 2024-09-06 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortvideo', '0020_alter_shortvideo_short_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortvideo',
            name='short_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 6, 12, 33, 54, 969820)),
        ),
    ]
