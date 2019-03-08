from django.db import models
from record.models import Level, Achievement


# Create your models here.
class Student(models.Model):
    school_organisation_id = models.PositiveIntegerField("The Related School Organisation")
    reg_num = models.CharField("Student's Unique Registeration number (produced after successful enrolment)",
                                  null=True, blank=True, max_length=20, unique=True)
    first_name = models.CharField('Student\'s first name', max_length=25)
    last_name = models.CharField('Student\'s Surname', max_length=25)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name="The Student's current level",
                              null=True, blank=True)
    profile_pic = models.CharField("Student profile picture", max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}:{2} (Level: {3})".format(self.first_name, self.last_name, self.reg_num, self.level)

    class Meta:
        ordering = ('-updated_at',)


class Parent(models.Model):
    school_organisation_id = models.PositiveIntegerField("The Related Organisation")
    students = models.ManyToManyField(Student, related_name='students', verbose_name="Students belonging to this parent")
    user_id = models.PositiveIntegerField("Parent's related Id on User Service", unique=True)
    home_addr = models.TextField(verbose_name="Home Address")
    emergency_numbers = models.TextField("Enter comma separated numbers in case of emergency", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ('-updated_at',)


class StudentAchievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Related student")
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, related_name='student_achievements',
                                    verbose_name="Achievements gotten by student")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Student: {}\nAchievements: {}".format(self.student, self.achievements)

    class Meta:
        db_table = "student_achievements"
        ordering = ('-updated_at',)
