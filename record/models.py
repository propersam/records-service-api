from django.db import models
from school.models import School


# Create your models here.
class Session(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="The Related School")
    session_name = models.CharField("Name of Session", max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_name


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

    def __str__(self):
        return self.term


class Level(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='related session for level')
    level_name = models.CharField("Name of Level", unique=True, max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level_name


class Group(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='related school for group')
    group_name = models.CharField("group name", max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_name


class Subject(models.Model):
    subject_name = models.CharField("Name of School subject", max_length=50)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='related level offering subject', null=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name='term in which subject is offered')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='specific group from level', null=True)
    description = models.TextField("Short subject description", null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name

