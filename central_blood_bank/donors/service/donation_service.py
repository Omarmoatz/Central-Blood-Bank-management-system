import logging
from datetime import date

from django.core.mail import send_mail

from central_blood_bank.donors.models import Donor
from central_blood_bank.donors.service.blood_stock_service import BloodStockService
from central_blood_bank.donors.tasks import manage_donation

logger = logging.getLogger(__name__)


class DonationService:
    def evaluate_and_store_donation(self, donor_id):
        donor = Donor.objects.get(id=donor_id)
        if donor.last_donation and (date.today() - donor.last_donation).days < 90:
            send_mail(
                "Donation Rejected",
                "Your donation is rejected "
                "due to insufficient time gap since last donation.",
                "noreply@bloodbank.com",
                [donor.email],
                fail_silently=False,
            )
            logger.warning(
                f"Donation rejected for {donor.name} ({donor.national_id})"
                "Less than 3 months since last donation.",
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
                f"Donation rejected for {donor.name} ({donor.national_id})"
                "Positive virus test.",
            )
            return "Donation rejected: Positive virus test."

        BloodStockService(donor).create_blood_stock()
        logger.info(
            f"Donation accepted for {donor.name} ({donor.national_id})"
            "Blood stock created.",
        )
        return "Donation accepted and added to stock."

    def handle_donation(self, donor_id):
        manage_donation.delay(donor_id)
