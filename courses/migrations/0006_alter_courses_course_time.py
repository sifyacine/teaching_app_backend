# Generated by Django 5.0.7 on 2024-08-12 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_courses_course_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 13, 0, 29, 57, 995185)),
        ),
    ]
