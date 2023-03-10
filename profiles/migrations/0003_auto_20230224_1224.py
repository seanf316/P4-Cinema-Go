# Generated by Django 3.2.17 on 2023-02-24 12:24

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20230222_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='director',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='fav_movie',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/seanf316/image/upload/v1677195145/Cinema-Go/default_profile_llyxo2.webp', max_length=255, verbose_name='image'),
        ),
    ]
