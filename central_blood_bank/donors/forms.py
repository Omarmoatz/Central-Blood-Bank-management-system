from django import forms
from central_blood_bank.donors.models import Donor

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'