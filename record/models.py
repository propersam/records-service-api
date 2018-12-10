from django.db import models


# Create your models here.
class School(models.Model):
    school_name = models.CharField('Name of the School', max_length=50)
    school_website = models.CharField("School's website", max_length=50)
    about_school = models.TextField("A Little About the School")
    school_address = models.CharField("Address of the School", max_length=120)
    school_phone = models.CharField("School Phone number", unique=True, max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Session(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="The Related School")
    session_name = models.CharField("Name of Session", max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Term(models.Model):
    AVAILABLE_TERMS = (
        (1, 'FIRST TERM'),
        (2, 'SECOND TERM'),
        (3, 'THIRD TERM'),
    )
    school = models.ForeignKey(School, null=True, on_delete=models.CASCADE, verbose_name='related school')
    term = models.IntegerField('term type', choices=AVAILABLE_TERMS)
    start_date = models.DateField("Starting of term date", null=True)
    end_date = models.DateField("Ending of term date", null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Level(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='related session for level')
    level_name = models.CharField("Name of Level", unique=True, max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Group(models.Model):
    group_name = models.CharField("group name", max_length=50)
    level = models.ForeignKey(Level, null=True, on_delete=models.CASCADE, verbose_name='Group related level')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='related school')
    subject_name = models.CharField("Name of School subject", max_length=50)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='related level offering subject', null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='specific group from level', null=True)
    description = models.TextField("Short subject description", null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
