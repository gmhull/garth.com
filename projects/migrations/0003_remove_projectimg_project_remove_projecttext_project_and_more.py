# Generated by Django 4.1.4 on 2023-06-13 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_projecttext_projectimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimg',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projecttext',
            name='project',
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='projectimg',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.projectpage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projecttext',
            name='page',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='projects.projectpage'),
            preserve_default=False,
        ),
    ]
