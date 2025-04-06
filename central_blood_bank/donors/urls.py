from rest_framework.routers import DefaultRouter

from central_blood_bank.donors.api.views import BloodStockViewSet
from central_blood_bank.donors.api.views import DonorViewSet

router = DefaultRouter()
router.register("donors", DonorViewSet, basename="donor")

urlpatterns = router.urls
app_name = "donors"
