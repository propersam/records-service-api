# Generated by Django 2.1.4 on 2019-01-28 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('record', '0001_firstMIgration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_organisation_id', models.PositiveIntegerField(verbose_name='The Related Organisation')),
                ('user_id', models.PositiveIntegerField(unique=True, verbose_name="Parent's related Id on User Service")),
                ('home_addr', models.TextField(verbose_name='Home Address')),
                ('emergency_numbers', models.TextField(max_length=50, verbose_name='Enter comma separated numbers in case of emergency')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_organisation_id', models.PositiveIntegerField(verbose_name='The Related School Organisation')),
                ('reg_num', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name="Student's Unique Registeration number (produced after successful enrolment)")),
                ('first_name', models.CharField(max_length=25, verbose_name="Student's first name")),
                ('last_name', models.CharField(max_length=25, verbose_name="Student's Surname")),
                ('profile_pic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Student profile picture')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Level', verbose_name="The Student's current level")),
            ],
            options={
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='StudentAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('achievements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_achievements', to='record.Achievement', verbose_name='Achievements gotten by student')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student', verbose_name='Related student')),
            ],
            options={
                'db_table': 'student_achievements',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.AddField(
            model_name='parent',
            name='students',
            field=models.ManyToManyField(related_name='students', to='student.Student', verbose_name='Students belonging to this parent'),
        ),
    ]