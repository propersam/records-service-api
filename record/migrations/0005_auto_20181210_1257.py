# Generated by Django 2.1.4 on 2018-12-10 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_auto_20181208_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ('date_created',)},
        ),
        migrations.RemoveField(
            model_name='school',
            name='date_joined',
        ),
        migrations.AddField(
            model_name='group',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='about_school',
            field=models.TextField(verbose_name='A Little About the School'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(verbose_name='Short subject description'),
        ),
    ]
