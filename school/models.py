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


class Staff(models.Model):
    """
        Model that controls Staff Table
    """
    # STAFF_TYPES = (
    #     ('HT', 'Head Teacher'),
    #     ('T', 'Teacher'),
    #     ('AT', 'Assistant Teacher'),
    #     ('B', 'Bursar'),
    #     ('O', 'Others')
    # )

    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='The School that staff belongs to')
    first_name = models.CharField('Staff\'s first name', max_length=25)
    last_name = models.CharField("Staff's Sur Name", max_length=25)
    gender = models.CharField("Teacher's gender", choices=GENDER_OPTIONS, max_length=5)
    phone = models.CharField("Staff's contact phone number", max_length=25)
    email = models.CharField("Staff's working email", max_length=50, null=True)
    # staff_type = models.CharField('The role of the staff', choices=STAFF_TYPES, max_length=5)
    profile_pics = models.CharField('profile picture of staff', max_length=50, null=True, blank=True)
    date_employed = models.DateField(null=True, blank=True)
    date_relieved = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)

    class Meta:
        ordering = ('-created_at',)

