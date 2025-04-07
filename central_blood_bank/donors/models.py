from datetime import date
from datetime import timedelta

from django.db import models


class BloodTypeChoices(models.TextChoices):
    A_POSITIVE = "A+", "A+"
    A_NEGATIVE = "A-", "A-"
    B_POSITIVE = "B+", "B+"
    B_NEGATIVE = "B-", "B-"
    AB_POSITIVE = "AB+", "AB+"
    AB_NEGATIVE = "AB-", "AB-"
    O_POSITIVE = "O+", "O+"
    O_NEGATIVE = "O-", "O-"


class Donor(models.Model):
    national_id = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    last_donation = models.DateField(null=True, blank=True)
    blood_type = models.CharField(choices=BloodTypeChoices, max_length=3)
    virus_test_result = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donors"
        ordering = ["name"]
        unique_together = ("national_id", "email")

    def __str__(self):
        return f"{self.name} ({self.national_id})"


class BloodStock(models.Model):
    blood_type = models.CharField(choices=BloodTypeChoices, max_length=3)
    city = models.CharField(max_length=50)
    expiration_date = models.DateField()
    donor = models.ForeignKey(
        Donor,
        on_delete=models.CASCADE,
        related_name="blood_stocks",
    )

    class Meta:
        verbose_name = "Blood Stock"
        verbose_name_plural = "Blood Stocks"

    def __str__(self):
        return f"{self.blood_type} - {self.city} - {self.expiration_date}"

    def save(self, *args, **kwargs):
        if not self.expiration_date:
            self.expiration_date = date.today() + timedelta(days=42)

        super().save(*args, **kwargs)
