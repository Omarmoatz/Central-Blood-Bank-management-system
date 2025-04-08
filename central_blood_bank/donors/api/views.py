from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from central_blood_bank.donors.api.serializers import BloodStockSerializer
from central_blood_bank.donors.api.serializers import DonorCreateUpdateSerializer
from central_blood_bank.donors.api.serializers import DonorListSerializer
from central_blood_bank.donors.api.serializers import EmptySerializer
from central_blood_bank.donors.models import BloodStock
from central_blood_bank.donors.models import Donor
from central_blood_bank.donors.services.donation_service import DonationService


class DonorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Donor.objects.all()
    serializer_class = DonorListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return DonorListSerializer
        if self.action in ["create", "update", "partial_update"]:
            return DonorCreateUpdateSerializer
        if self.action == "donate":
            return EmptySerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["post"])
    def donate(self, request, *args, **kwargs):
        donor_id = self.kwargs["pk"]
        DonationService().handle_donation(donor_id)
        return Response({"message": "Donation In Progress!"}, status=200)


class BloodStockViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = BloodStock.objects.all()
    serializer_class = BloodStockSerializer
