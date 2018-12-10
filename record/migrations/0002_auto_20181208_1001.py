# Generated by Django 2.1.4 on 2018-12-08 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='level_id',
        ),
        migrations.AddField(
            model_name='group',
            name='group_levels',
            field=models.ManyToManyField(to='record.Level'),
        ),
        migrations.AddField(
            model_name='school',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]