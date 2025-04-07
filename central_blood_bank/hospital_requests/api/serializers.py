from rest_framework import serializers

from central_blood_bank.hospital_requests.models import HospitalRequest

class HospitalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRequest
        fields = '__all__'