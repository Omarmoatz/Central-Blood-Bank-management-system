from celery import shared_task


@shared_task
def process_hospital_requests():
    from .services.request_service import RequestService

    return RequestService.fulfill_pending_requests()
