from django.db import models


# Create your models here.

class StaffContract(models.Model):


class StaffDepartment(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="School that own this staff department")
    department = models.CharField("Staff Department", max_length=150)
    description


