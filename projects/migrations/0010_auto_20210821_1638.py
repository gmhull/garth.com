# Generated by Django 3.2.5 on 2021-08-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20210821_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover_image',
            field=models.ImageField(upload_to=models.SlugField(max_length=140, unique=True)),
        ),
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.ImageField(default='Default.png', upload_to=models.SlugField(max_length=140, unique=True)),
        ),
        migrations.AlterField(
            model_name='project',
            name='img2',
            field=models.ImageField(default='Default.png', upload_to=models.SlugField(max_length=140, unique=True)),
        ),
        migrations.AlterField(
            model_name='project',
            name='img3',
            field=models.ImageField(default='Default.png', upload_to=models.SlugField(max_length=140, unique=True)),
        ),
        migrations.AlterField(
            model_name='project',
            name='img4',
            field=models.ImageField(default='Default.png', upload_to=models.SlugField(max_length=140, unique=True)),
        ),
        migrations.AlterField(
            model_name='project',
            name='img5',
            field=models.ImageField(default='Default.png', upload_to=models.SlugField(max_length=140, unique=True)),
        ),
    ]