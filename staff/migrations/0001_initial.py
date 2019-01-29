# Generated by Django 2.1.4 on 2019-01-29 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_id', models.PositiveIntegerField(verbose_name='The Organisation were staff contract belongs to.')),
                ('staff_id', models.PositiveIntegerField(verbose_name='User ID of user with role Staff')),
                ('start_date', models.DateField(verbose_name="Starting date of staff's contract")),
                ('end_data', models.DateField(verbose_name='Contract termination/end date')),
                ('end_of_trial', models.DateField(blank=True, null=True, verbose_name='Date when trial period ends')),
                ('work_schedule', models.CharField(max_length=50, verbose_name='Working hours')),
                ('salary', models.IntegerField(verbose_name="Staff's monthly wage in contract duration")),
                ('contract_state', models.CharField(choices=[('new', 'NEW'), ('running', 'RUNNING'), ('expired', 'EXPIRED'), ('to renew', 'TO RENEW')], default='new', max_length=20, verbose_name='State of Staff Contract')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_id', models.PositiveIntegerField(verbose_name='Organisation that own this staff department')),
                ('department', models.CharField(max_length=150, verbose_name='Staff Department')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description about department')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_id', models.PositiveIntegerField(verbose_name='Organisation that own this staff department')),
                ('level', models.CharField(max_length=150, verbose_name='Staff Level')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description about level')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_id', models.PositiveIntegerField(verbose_name='Organisation that own this staff department')),
                ('position', models.CharField(max_length=150, verbose_name='Staff Position')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description about department')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='staffcontract',
            name='staff_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.StaffDepartment', verbose_name='Department staff is assigned to'),
        ),
        migrations.AddField(
            model_name='staffcontract',
            name='staff_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.StaffLevel', verbose_name="Staff's overall level in the organisation"),
        ),
        migrations.AddField(
            model_name='staffcontract',
            name='staff_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.StaffPosition', verbose_name="Staff's Assigned job position"),
        ),
    ]
