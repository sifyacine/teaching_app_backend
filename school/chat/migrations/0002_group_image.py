# Generated by Django 4.2.15 on 2024-08-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='group_images/'),
        ),
    ]