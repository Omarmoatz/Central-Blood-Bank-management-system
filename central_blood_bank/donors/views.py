from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

from central_blood_bank.donors.models import Donor
from central_blood_bank.donors.forms import DonorForm
from central_blood_bank.donors.services.donation_service import DonationService

class DonorListView(generic.ListView):
    model = Donor

class DonorRegisterView(FormView):
    template_name = 'donor_register.html'
    form_class = DonorForm
    success_url = reverse_lazy('donation_result')

    def form_valid(self, form):
        donor = form.save()
        self.request.session['donation_msg'] = DonationService().evaluate_and_store_donation(donor.id)
        return super().form_valid(form)
    
class DonationResultView(TemplateView):
    template_name = 'donation_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = self.request.session.pop('donation_msg', 'No result available.')
        return context