from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


from central_blood_bank.donors.models import Donor, BloodStock
from central_blood_bank.donors.forms import DonorForm
from central_blood_bank.donors.services.donation_service import DonationService

class DonorListView(LoginRequiredMixin, generic.ListView):
    model = Donor
    template_name = 'donors/donor_list.html'
    context_object_name = 'donors'
    paginate_by = 5

class DonorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Donor
    template_name = 'donors/donor_detail.html'
    context_object_name = 'donor'

class DonorRegisterView(LoginRequiredMixin, FormView):
    template_name = 'donors/donor_register.html'
    form_class = DonorForm
    success_url = reverse_lazy('donors:donor_list')

    def form_valid(self, form):
        donor = form.save()
        result = DonationService().evaluate_and_store_donation(donor.id)
        messages.success(self.request, result)
        return super().form_valid(form)

class BloodStockListView(LoginRequiredMixin, generic.ListView):
    model = BloodStock
    template_name = 'donors/blood_stock_list.html'
    context_object_name = 'stocks'