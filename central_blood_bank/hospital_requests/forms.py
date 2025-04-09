from django import forms

from central_blood_bank.hospital_requests.models import HospitalRequest


class HospitalRequestForm(forms.ModelForm):
    class Meta:
        model = HospitalRequest
        fields = (
            "hospital_name",
            "blood_type",
            "city",
            "urgency_level",
        )