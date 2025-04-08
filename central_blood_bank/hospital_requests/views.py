from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import HospitalRequestForm
from .models import HospitalRequest
from .services.request_service import RequestService


class HospitalRequestView(FormView):
    template_name = 'hospital_request.html'
    form_class = HospitalRequestForm
    success_url = reverse_lazy('hospital_request')

    def form_valid(self, form):
        form.save()
        if HospitalRequest.objects.filter(status=HospitalRequest.StatusChoices.PENDING).count() >= 10:
            RequestService().handle_hospital_request_queue()
        return super().form_valid(form)
