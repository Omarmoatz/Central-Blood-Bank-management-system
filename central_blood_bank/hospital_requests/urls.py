from rest_framework.routers import DefaultRouter

from central_blood_bank.hospital_requests.api.views import HospitalRequestViewSet

router = DefaultRouter()
router.register(
    "hospital-requests",
    HospitalRequestViewSet,
    basename="hospital-requests",
)

urlpatterns = router.urls
app_name = "hospital_requests"
