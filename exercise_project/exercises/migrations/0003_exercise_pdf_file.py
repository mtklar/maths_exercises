# Generated by Django 4.2.3 on 2023-07-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_remove_exercise_year_exercise_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='pdf_file',
            field=models.FileField(default=1, upload_to='pdfs/'),
            preserve_default=False,
        ),
    ]
