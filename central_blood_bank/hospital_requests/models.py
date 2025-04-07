from django.db import models

from central_blood_bank.donors.models import BloodTypeChoices

class HospitalRequest(models.Model):
    class UrgencyLevelChoices(models.TextChoices):
        IMMEDIATE = "Immediate", "Immediate"
        URGENT = "Urgent", "Urgent"
        NORMAL = "Normal", "Normal"
    
    class StatusChoices(models.TextChoices):
        PENDING = "Pending", "Pending"
        APPROVED = "Approved", "Approved"
        REJECTED = "Rejected", "Rejected"

    hospital_name = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3, choices=BloodTypeChoices.choices)
    city = models.CharField(max_length=50)
    urgency_level = models.CharField(max_length=10, choices=UrgencyLevelChoices.choices)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)

    def __str__(self):
        return f"{self.hospital_name} - {self.blood_type}"
