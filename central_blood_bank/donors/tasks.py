from datetime import date, timedelta
from celery import shared_task
from django.core.mail import send_mail

from central_blood_bank.donors.models import BloodStock, Donor


@shared_task
def manage_donation(donor_id):
    donor = Donor.objects.get(id=donor_id)
    if donor.last_donation and (date.today() - donor.last_donation).days < 90:
        send_mail(
            'Donation Rejected',
            'Your donation is rejected due to insufficient time gap since last donation.',
            'noreply@bloodbank.com',
            [donor.email],
            fail_silently=False,
        )
        return "Donation rejected: Less than 3 months since last donation."
    elif not donor.virus_test_result:
        send_mail(
            'Donation Rejected',
            'Your donation is rejected due to a positive virus test.',
            'noreply@bloodbank.com',
            [donor.email],
            fail_silently=False,
        )
        return "Donation rejected: Positive virus test."
    
    BloodStock.objects.create(
        blood_type=donor.blood_type,
        city=donor.city,
        expiration_date=date.today() + timedelta(days=42),
        donor=donor
    )
    return "Donation accepted and added to stock."