from django.db import models

from central_blood_bank.donors.models import BloodTypeChoices, CityChoices
from django.core.validators import EmailValidator

class HospitalRequest(models.Model):
    class UrgencyLevelChoices(models.TextChoices):
        IMMEDIATE = "Immediate", "Immediate"
        URGENT = "Urgent", "Urgent"
        NORMAL = "Normal", "Normal"

    class StatusChoices(models.TextChoices):
        PENDING = "Pending", "Pending"
        APPROVED = "Approved", "Approved"
        REJECTED = "Rejected", "Rejected"
        UNCOMPLETED = "Uncompleted", "Uncompleted"

    hospital_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    blood_type = models.CharField(max_length=3, choices=BloodTypeChoices.choices)
    city = models.CharField(max_length=50, choices=CityChoices.choices)
    urgency_level = models.CharField(max_length=10, choices=UrgencyLevelChoices.choices)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=12,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    def __str__(self):
        return f"{self.hospital_name} - {self.blood_type}"
