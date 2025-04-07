import logging
# from datetime import date

from celery import shared_task
from central_blood_bank.hospital_requests.service.request_service import RequestService


@shared_task
def process_hospital_requests():
    return RequestService().fulfill_pending_requests()