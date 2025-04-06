from rest_framework import serializers

from central_blood_bank.donors.models import BloodStock
from central_blood_bank.donors.models import Donor


class DonorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = "__all__"


class DonorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = (
            "name",
            "national_id",
            "email",
            "city",
            "blood_type",
            "last_donation",
            "virus_test_result",
        )
        extra_kwargs = {
            "last_donation": {"required": True},
            "virus_test_result": {"required": True},
        }


class BloodStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodStock
        fields = "__all__"
