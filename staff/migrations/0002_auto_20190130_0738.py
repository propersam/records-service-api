# Generated by Django 2.1.4 on 2019-01-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffcontract',
            old_name='end_data',
            new_name='end_date',
        ),
        migrations.AlterField(
            model_name='stafflevel',
            name='organisation_id',
            field=models.PositiveIntegerField(verbose_name='Organisation that own this staff Level'),
        ),
        migrations.AlterField(
            model_name='staffposition',
            name='organisation_id',
            field=models.PositiveIntegerField(verbose_name='Organisation that own this staff Position'),
        ),
    ]
