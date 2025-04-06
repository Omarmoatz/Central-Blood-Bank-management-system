from rest_framework import mixins
from rest_framework import viewsets

from central_blood_bank.donors.api.serializers import BloodStockSerializer
from central_blood_bank.donors.api.serializers import DonorCreateSerializer
from central_blood_bank.donors.api.serializers import DonorListSerializer
from central_blood_bank.donors.models import BloodStock
from central_blood_bank.donors.models import Donor


class DonorViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Donor.objects.all()
    serializer_class = DonorListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return DonorListSerializer
        if self.action == "create":
            return DonorCreateSerializer
        return super().get_serializer_class()

