# Generated by Django 2.2.16 on 2022-04-19 10:11

import reviews.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20220419_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.models.year_validator]),
        ),
    ]
