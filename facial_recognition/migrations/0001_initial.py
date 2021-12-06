# Generated by Django 3.2.5 on 2021-12-03 02:54

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='dnd')),
                ('face_encoding', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=128)),
            ],
        ),
    ]
