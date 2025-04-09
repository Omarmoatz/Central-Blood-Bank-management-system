from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from central_blood_bank.donors.models import Donor
from central_blood_bank.donors.forms import DonorForm
from central_blood_bank.donors.services.donation_service import DonationService

class DonorListView(generic.ListView):
    model = Donor
    template_name = 'donors/donor_list.html'
    context_object_name = 'donors'
    paginate_by = 5

class DonorDetailView(generic.DetailView):
    model = Donor
    template_name = 'donors/donor_detail.html'
    context_object_name = 'donor'

class DonorRegisterView(FormView):
    template_name = 'donors/donor_register.html'
    form_class = DonorForm
    success_url = reverse_lazy('donors:donor_list')

    def form_valid(self, form):
        donor = form.save()
        result = DonationService().evaluate_and_store_donation(donor.id)
        messages.success(self.request, result)
        return super().form_valid(form)
