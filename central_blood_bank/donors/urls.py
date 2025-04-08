from django.urls import path
from rest_framework.routers import DefaultRouter

from central_blood_bank.donors.api.views import BloodStockViewSet
from central_blood_bank.donors.api.views import DonorViewSet
from central_blood_bank.donors.views import DonationResultView, DonorRegisterView

router = DefaultRouter()
router.register("donors", DonorViewSet, basename="donor")
router.register("blood-stocks", BloodStockViewSet, basename="blood-stock")

urlpatterns = [
    path('donor/register/', DonorRegisterView.as_view(), name='donor_register'),
    path('donor/result/', DonationResultView.as_view(), name='donation_result'),

    *router.urls
]
app_name = "donors"
