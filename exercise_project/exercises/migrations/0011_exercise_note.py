# Generated by Django 4.2.3 on 2023-09-08 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0010_remove_tag_exercises_exercise_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='note',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]