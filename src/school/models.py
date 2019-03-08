from django.db import models


# Create your models here.
class School(models.Model):

    """
        Model that controls School Table
    """
    school_name = models.CharField('Name of the School', max_length=50)
    school_website = models.CharField("School's website", max_length=50)
    about_school = models.TextField("A Little About the School")
    school_address = models.CharField("Address of the School", max_length=120)
    school_phone = models.CharField("School Phone number", unique=True, max_length=20)
    school_logo = models.CharField("School Logo", default="default_png_logo_address", max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ('-updated_at',)
        db_table = 'school'

