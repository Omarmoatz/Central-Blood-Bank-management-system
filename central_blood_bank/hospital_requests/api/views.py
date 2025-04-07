from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from central_blood_bank.hospital_requests.models import HospitalRequest
from central_blood_bank.hospital_requests.api.serializers import (
    HospitalRequestRetrieveSerializer,
    HospitalRequestCreateSerializer
)
from central_blood_bank.hospital_requests.service.request_service import RequestService

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


