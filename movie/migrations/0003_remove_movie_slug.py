# Generated by Django 3.2.17 on 2023-02-20 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_movieid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Slug',
        ),
    ]
