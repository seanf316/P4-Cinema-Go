# Generated by Django 3.2.17 on 2023-03-22 01:13

import django.core.validators
from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_alter_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=djrichtextfield.models.RichTextField(null=True, validators=[django.core.validators.MaxLengthValidator(2500)]),
        ),
    ]
