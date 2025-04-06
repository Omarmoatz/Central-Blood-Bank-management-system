from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from central_blood_bank.donors.api.serializers import BloodStockSerializer
from central_blood_bank.donors.api.serializers import DonorCreateSerializer
from central_blood_bank.donors.api.serializers import DonorListSerializer
from central_blood_bank.donors.models import BloodStock
from central_blood_bank.donors.models import Donor
from central_blood_bank.donors.tasks import manage_donation


class DonorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.updateModelMixin,
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
    
    @action(detail=True, methods=["post"])
    def donate(self, request, *args, **kwargs):
        donor_id = self.kwargs["pk"]
        manage_donation.delay(donor_id)
        return Response({"message": "Donation successful!"}, status=200)

class BloodStockViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = BloodStock.objects.all()
    serializer_class = BloodStockSerializer
