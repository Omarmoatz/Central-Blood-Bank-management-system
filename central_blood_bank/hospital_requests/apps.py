import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HospitalRequestConfig(AppConfig):
    name = "central_blood_bank.hospital_requests"
    verbose_name = _("Hospital Request")

    def ready(self):
        with contextlib.suppress(ImportError):
            import central_blood_bank.hospital_requests.signals  # noqa: F401
