from django.db import models
from school.models import School


# Create your models here.
class Session(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="The Related School")
    session_name = models.CharField("Name of Session", max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.session_name

    class Meta:
        ordering = ('-created_at',)


class Term(models.Model):
    AVAILABLE_TERMS = (
        (1, 'FIRST TERM'),
        (2, 'SECOND TERM'),
        (3, 'THIRD TERM'),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='related school')
    term = models.IntegerField('term type', choices=AVAILABLE_TERMS)
    start_date = models.DateField("Starting of term date", null=True, blank=True)
    end_date = models.DateField("Ending of term date", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.AVAILABLE_TERMS[self.term-1]

    class Meta:
        ordering = ('-created_at',)


class Level(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, verbose_name='related session for level')
    level_name = models.CharField("Name of Level", unique=True, max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level_name

    class Meta:
        ordering = ('-created_at',)


class Group(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='level that group belongs to', null=True)
    group_name = models.CharField("group name", unique=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ('-created_at',)


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="School where subject is offered")
    levels = models.ManyToManyField(Level, verbose_name='levels offering subject')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name='term in which subject is offered')
    groups = models.ManyToManyField(Group, verbose_name='groups offering subject')
    subject_name = models.CharField("Name of School subject", unique=True, max_length=50)
    description = models.TextField("Short description for subject", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name

    class Meta:
        ordering = ('-updated_at',)


class Achievement(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="School where the achievement exists")
    name = models.CharField("The name of the achievement", max_length=50)
    value = models.IntegerField("The numeric value attached to this achievement")
    level = models.ForeignKey(Level, on_delete="models.CASCADE",
                              verbose_name="The level that the achievement belongs to", blank=True, null=True)
    # default level '0' stands for all levels
    description = models.TextField("A Description of the achievement")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Achievement name: "+self.name

    class Meta:
        ordering = ('-updated_at',)

