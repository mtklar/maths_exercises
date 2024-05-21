# Generated by Django 4.2.3 on 2023-07-25 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='year',
        ),
        migrations.AddField(
            model_name='exercise',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date created'),
            preserve_default=False,
        ),
    ]
