# Generated by Django 3.0.8 on 2021-06-15 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='slug',
            field=models.SlugField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]