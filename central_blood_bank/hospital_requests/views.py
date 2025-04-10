from django.contrib import messages
from django.views import generic
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import HospitalRequestForm
from .models import HospitalRequest
from .services.request_service import RequestService


class HospitalRequestListView(LoginRequiredMixin, generic.ListView):
    model = HospitalRequest
    template_name = 'hospital_requests/hospital_request_list.html'
    context_object_name = 'requests'
    paginate_by = 20

class HospitalRequestView(FormView):
    template_name = 'hospital_requests/hospital_request.html'
    form_class = HospitalRequestForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        if HospitalRequest.objects.filter(status=HospitalRequest.StatusChoices.PENDING).count() >= 10:
            RequestService.handle_hospital_request_queue()
        messages.success(self.request, "successfully created your request we will inform you via your email after finishing the request")
        return super().form_valid(form)
