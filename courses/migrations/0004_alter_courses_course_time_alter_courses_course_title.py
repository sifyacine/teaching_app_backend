# Generated by Django 5.0.7 on 2024-08-09 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_courses_course_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 15, 3, 35, 496219)),
        ),
        migrations.AlterField(
            model_name='courses',
            name='course_title',
            field=models.CharField(max_length=50),
        ),
    ]
