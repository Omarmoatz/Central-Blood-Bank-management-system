from rest_framework import mixins
from rest_framework import viewsets

from central_blood_bank.hospital_requests.api.serializers import (
    HospitalRequestCreateSerializer,
)
from central_blood_bank.hospital_requests.api.serializers import (
    HospitalRequestRetrieveSerializer,
)
from central_blood_bank.hospital_requests.models import HospitalRequest


class HospitalRequestViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = HospitalRequest.objects.all()
    serializer_class = HospitalRequestRetrieveSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return HospitalRequestRetrieveSerializer
        if self.action == "create":
            return HospitalRequestCreateSerializer
        return super().get_serializer_class()
