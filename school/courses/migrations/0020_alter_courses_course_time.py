# Generated by Django 5.0.7 on 2024-09-07 22:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_alter_courses_course_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 7, 23, 37, 5, 157204)),
        ),
    ]