# Generated by Django 2.2.16 on 2022-04-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220419_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(db_index=True, max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(db_index=True, max_length=256),
        ),
    ]
