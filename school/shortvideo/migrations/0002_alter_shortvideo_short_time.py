# Generated by Django 5.0.7 on 2024-08-07 23:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortvideo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortvideo',
            name='short_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 8, 0, 20, 25, 322953)),
        ),
    ]
