# Generated by Django 3.2.17 on 2023-03-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_text_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(blank=True, max_length=2500, null=True),
        ),
    ]