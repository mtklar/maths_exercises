# Generated by Django 4.2.3 on 2023-09-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='exercises',
            field=models.ManyToManyField(to='exercises.exercise'),
        ),
    ]
