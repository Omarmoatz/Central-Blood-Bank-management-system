import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def manage_donation(donor_id):
    from .service.donation_service import DonationService

    return DonationService().evaluate_and_store_donation(donor_id)
