from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from central_blood_bank.hospital_requests.models import HospitalRequest
from central_blood_bank.hospital_requests.api.serializers import (
    HospitalRequestSerializer,
)


class HospitalRequestViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = HospitalRequest.objects.all()
    serializer_class = HospitalRequestSerializer

#     def get_serializer_class(self):
#         if self.action == "list":
#             return DonorListSerializer
#         if self.action in ["create", "update", "partial_update"]:
#             return DonorCreateUpdateSerializer
#         if self.action == "donate":
#             return EmptySerializer
#         return super().get_serializer_class()


