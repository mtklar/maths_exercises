# Generated by Django 4.2.3 on 2023-08-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_exercise_png_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('png_file', models.ImageField(upload_to='pngs/')),
            ],
        ),
        migrations.AlterField(
            model_name='exercise',
            name='text',
            field=models.TextField(),
        ),
    ]
