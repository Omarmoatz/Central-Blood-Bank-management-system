import logging

from central_blood_bank.donors.models import BloodStock
from central_blood_bank.hospital_requests.models import HospitalRequest
from central_blood_bank.hospital_requests.tasks import process_hospital_requests

logger = logging.getLogger(__name__)


class RequestService:
    def fulfill_pending_requests(self):
        requests = HospitalRequest.objects.filter(
            status=HospitalRequest.StatusChoices.PENDING,
        )
        for request in requests:
            stock = BloodStock.objects.filter(
                blood_type=request.blood_type,
                city=request.city,
            ).first()
            if stock:
                stock.delete()
                request.status = HospitalRequest.StatusChoices.APPROVED
                request.save()
                logger.info(f"Request {request.id} approved and stock deleted.")

            else:
                request.status = HospitalRequest.StatusChoices.REJECTED
                request.save()
                logger.info(f"Request {request.id} rejected due to insufficient stock.")

        logger.info(f"Processed {len(requests)} hospital requests.")
        return "Hospital requests processed."

    def handle_hospital_request_queue(self):
        process_hospital_requests.delay()
