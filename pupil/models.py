from django.db import models
from school.models import School
from record.models import Level, Achievement


# Create your models here.
class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='The School where the student belongs')
    unique_tag = models.CharField("Student's Unique ID tag (produced after successful enrolment)",
                                  null=True, blank=True, max_length=20)
    first_name = models.CharField('Students first name', max_length=25)
    last_name = models.CharField('Students Surname', max_length=25)
    enrolled_level = models.ForeignKey(Level, on_delete=models.CASCADE,
                                       null=True, verbose_name="The Level student was first Enrolled In")
    current_level = models.CharField("The Student's current level", max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} (level: {})".format(self.first_name, self.last_name, self.current_level)

    class Meta:
        ordering = ('-updated_at',)


class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Students belonging to this parent")
    full_name = models.CharField('Parent Full name', max_length=50)
    phone_num = models.CharField("Parent contact number", max_length=20)
    email = models.CharField("Parent Email Address", max_length=50, null=True, blank=True)
    home_addr = models.TextField(verbose_name="Home Address")
    emergency_numbers = models.TextField("Enter comma separated numbers in case of emergency", max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('-updated_at',)


class StudentAchievement(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Related student")
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE,
                                    verbose_name="Achievement gotten by student")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Student: {}\nAchievement: {}".format(self.student, self.achievement)

    class Meta:
        db_table = "student_achievement"
        ordering = ('-updated_at',)
