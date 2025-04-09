from django.urls import path
from rest_framework.routers import DefaultRouter

from central_blood_bank.hospital_requests.api.views import HospitalRequestViewSet
from central_blood_bank.hospital_requests.views import HospitalRequestListView, HospitalRequestView

router = DefaultRouter()
router.register(
    "hospital-requests",
    HospitalRequestViewSet,
    basename="hospital-requests",
)

urlpatterns = [
    path('', HospitalRequestListView.as_view(), name='hospital_request_list'),
    path('create/', HospitalRequestView.as_view(), name='hospital_request'),
    
    *router.urls
]
app_name = "hospital_requests"
