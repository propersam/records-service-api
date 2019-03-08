from django.db import models


# Create your models here.

class StaffDepartment(models.Model):
    organisation_id = models.PositiveIntegerField(verbose_name="Organisation that own this staff department")
    department = models.CharField("Staff Department", max_length=150)
    description = models.TextField("Description about department", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department


class StaffPosition(models.Model):
    organisation_id = models.PositiveIntegerField(verbose_name="Organisation that own this staff Position")
    position = models.CharField("Staff Position", max_length=150)
    description = models.TextField("Description about department", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position


class StaffLevel(models.Model):
    organisation_id = models.PositiveIntegerField(verbose_name="Organisation that own this staff Level")
    level = models.CharField("Staff Level", max_length=150)
    description = models.TextField("Description about level", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.level


class StaffContract(models.Model):
    CONTRACT_STATES = (
        ('new', 'NEW'),
        ('running', 'RUNNING'),
        ('expired', 'EXPIRED'),
        ('to renew', 'TO RENEW'),
    )
    organisation_id = models.PositiveIntegerField(verbose_name="The Organisation were staff contract belongs to.")
    staff_id = models.PositiveIntegerField(verbose_name="User ID of user with role Staff")
    staff_department = models.ForeignKey(StaffDepartment, on_delete=models.CASCADE, verbose_name="Department staff is assigned to" )
    staff_position = models.ForeignKey(StaffPosition, on_delete=models.CASCADE, verbose_name="Staff's Assigned job position")
    staff_level = models.ForeignKey(StaffLevel, on_delete=models.CASCADE, verbose_name="Staff's overall level in the organisation")
    start_date = models.DateField(verbose_name="Starting date of staff's contract")
    end_date = models.DateField(verbose_name="Contract termination/end date")
    end_of_trial = models.DateField(verbose_name="Date when trial period ends", null=True, blank=True)
    work_schedule = models.CharField("Working hours", max_length=50)
    salary = models.IntegerField(verbose_name="Staff's monthly wage in contract duration")
    contract_state = models.CharField("State of Staff Contract", max_length=20, choices=CONTRACT_STATES, default = 'new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        "staff: {} -> department: {}".format(self.staff_id, self.staff_department)

