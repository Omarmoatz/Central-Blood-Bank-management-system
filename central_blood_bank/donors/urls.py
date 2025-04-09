from django.urls import path
from rest_framework.routers import DefaultRouter

from central_blood_bank.donors.api.views import BloodStockViewSet
from central_blood_bank.donors.api.views import DonorViewSet
from central_blood_bank.donors.views import BloodStockListView, DonorDetailView, DonorRegisterView, DonorListView

router = DefaultRouter()
router.register("donors", DonorViewSet, basename="donor")
router.register("blood-stocks", BloodStockViewSet, basename="blood-stock")

urlpatterns = [
    path('', DonorListView.as_view(), name='donor_list'),
    path('<int:pk>/', DonorDetailView.as_view(), name='donor_detail'),
    path('register/', DonorRegisterView.as_view(), name='donor_register'),
    path('stock/', BloodStockListView.as_view(), name='blood_stock_list'),

    *router.urls
]
app_name = "donors"
