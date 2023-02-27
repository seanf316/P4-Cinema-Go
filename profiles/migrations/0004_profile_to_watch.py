# Generated by Django 3.2.17 on 2023-02-26 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20230221_0043'),
        ('profiles', '0003_auto_20230224_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='to_watch',
            field=models.ManyToManyField(blank=True, related_name='to_watch', to='movie.Movie'),
        ),
    ]
