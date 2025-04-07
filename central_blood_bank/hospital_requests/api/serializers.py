from rest_framework import serializers

from central_blood_bank.hospital_requests.models import HospitalRequest
from central_blood_bank.hospital_requests.service.request_service import RequestService


class HospitalRequestRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRequest
        fields = '__all__'


class HospitalRequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalRequest
        fields = (
            "hospital_name",
            "blood_type",
            "city",
            "urgency_level",
        )

    def create(self, validated_data):
        RequestService().handle_hospital_requests()
        return super().create(validated_data)