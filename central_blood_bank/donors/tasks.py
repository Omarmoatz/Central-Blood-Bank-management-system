import logging
from datetime import date

from celery import shared_task
from django.core.mail import send_mail

from central_blood_bank.donors.models import Donor
from central_blood_bank.donors.service.blood_stock_service import BloodStockService

logger = logging.getLogger(__name__)


@shared_task
def manage_donation(donor_id):
    donor = Donor.objects.get(id=donor_id)
    if donor.last_donation and (date.today() - donor.last_donation).days < 90:
        send_mail(
            "Donation Rejected",
            "Your donation is rejected due to insufficient time gap since last donation.",
            "noreply@bloodbank.com",
            [donor.email],
            fail_silently=False,
        )
        logger.warning(
            f"Donation rejected for {donor.name} ({donor.national_id}): Less than 3 months since last donation."
        )
        return "Donation rejected: Less than 3 months since last donation."
    if not donor.virus_test_result:
        send_mail(
            "Donation Rejected",
            "Your donation is rejected due to a positive virus test.",
            "noreply@bloodbank.com",
            [donor.email],
            fail_silently=False,
        )
        logger.warning(
            f"Donation rejected for {donor.name} ({donor.national_id}): Positive virus test."
        )
        return "Donation rejected: Positive virus test."

    BloodStockService(donor).create_blood_stock()
    logger.info(
        f"Donation accepted for {donor.name} ({donor.national_id}). Blood stock created."
    )
    return "Donation accepted and added to stock."
