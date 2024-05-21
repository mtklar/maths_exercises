# Generated by Django 4.2.3 on 2023-09-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_tag_exercises'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='exercises',
        ),
        migrations.AddField(
            model_name='exercise',
            name='tags',
            field=models.ManyToManyField(to='exercises.tag'),
        ),
    ]