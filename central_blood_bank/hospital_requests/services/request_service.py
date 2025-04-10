import logging
from django.core.mail import send_mail
from operator import itemgetter

from central_blood_bank.donors.models import BloodStock
from central_blood_bank.hospital_requests.models import HospitalRequest
from central_blood_bank.hospital_requests.tasks import process_hospital_requests
from central_blood_bank.hospital_requests.utils import get_city_distance

logger = logging.getLogger(__name__)


class RequestService:
    
    @classmethod
    def fulfill_pending_requests(cls):
        requests = HospitalRequest.objects.filter(status=HospitalRequest.StatusChoices.PENDING)
        fulfilled = []

        for request in requests:
            needed = request.quantity
            stock_list = BloodStock.objects.filter(blood_type=request.blood_type)

            if not stock_list.exists():
                cls._notify(request, "Rejected", "No matching blood stock found.")
                continue

            distance_scored = [(s, get_city_distance(s.city, request.city)) for s in stock_list]
            distance_scored.sort(key=itemgetter(1))

            selected = []
            for s, _ in distance_scored:
                if needed == 0:
                    break
                selected.append(s)
                needed -= 1

            if len(selected) == request.quantity:
                status = HospitalRequest.StatusChoices.APPROVED
                for s in selected:
                    s.delete()
            elif selected:
                status = HospitalRequest.StatusChoices.UNCOMPLETED
                for s in selected:
                    s.delete()
            else:
                status = HospitalRequest.StatusChoices.REJECTED

            request.status = status
            request.save()
            fulfilled.append(request.id)
            cls._notify(request, status)

        return f"Processed {len(requests)} requests. Fulfilled: {len(fulfilled)}."

    @staticmethod
    def _notify(request, status, reason=None):
        subject = f"Blood Request Status: {status}"
        message = f"Hello {request.hospital_name},\n\n"
        if status == HospitalRequest.StatusChoices.APPROVED:
            message += f"Your blood request for {request.quantity} unit(s) of {request.blood_type} has been approved."
        elif status == HospitalRequest.StatusChoices.REJECTED:
            message += f"Unfortunately, your blood request for {request.blood_type} could not be fulfilled."
            if reason:
                message += f"\nReason: {reason}"
        elif status == HospitalRequest.StatusChoices.UNCOMPLETED:
            message += f"Your request for {request.quantity} unit(s) of {request.blood_type} was partially fulfilled due to limited stock."

        send_mail(
            subject,
            message,
            'noreply@bloodbank.com',
            [request.email],
            fail_silently=False,
        )
        logger.info(f"Notification sent to {request.hospital_name} about request status: {status}")

    @staticmethod
    def handle_hospital_request_queue():
        process_hospital_requests.delay()
