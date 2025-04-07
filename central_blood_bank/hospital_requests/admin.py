from django.contrib import admin

from central_blood_bank.hospital_requests.models import HospitalRequest


@admin.register(HospitalRequest)
class HospitalRequestAdmin(admin.ModelAdmin):
    list_display = [
        "hospital_name",
        "blood_type",
        "city",
        "urgency_level",
        "status",
    ]
    list_filter = ["blood_type", "city"]
    search_fields = ["hospital_name"]
