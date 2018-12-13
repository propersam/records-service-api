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

    def __str__(self):
        return self.school_name
