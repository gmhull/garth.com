# Generated by Django 3.0.8 on 2021-06-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeons', '0002_level_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='slug',
            field=models.SlugField(max_length=10, unique=True),
        ),
    ]
