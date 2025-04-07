import logging
from celery import shared_task

from central_blood_bank.donors.service.donation_service import DonationService

logger = logging.getLogger(__name__)


@shared_task
def manage_donation(donor_id):
    return DonationService().evaluate_and_store_donation(donor_id)
