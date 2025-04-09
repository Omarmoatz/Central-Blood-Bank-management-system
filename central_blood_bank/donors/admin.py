from django.contrib import admin

from central_blood_bank.donors.models import BloodStock
from central_blood_bank.donors.models import Donor


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "national_id",
        "email",
        "city",
        "blood_type",
        "last_donation",
        "virus_test_result"
    ]
    list_filter = ["blood_type", "city"]
    search_fields = ["name", "national_id", "email"]


@admin.register(BloodStock)
class BloodStockAdmin(admin.ModelAdmin):
    list_display = ["blood_type", "city", "expiration_date", "donor"]
    list_filter = ["blood_type", "city"]
    search_fields = ["blood_type", "donor", "city"]
    raw_id_fields = ["donor"]
