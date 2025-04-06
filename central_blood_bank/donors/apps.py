import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DonorsConfig(AppConfig):
    name = "central_blood_bank.donors"
    verbose_name = _("Donors")

    def ready(self):
        with contextlib.suppress(ImportError):
            import central_blood_bank.donors.signals  # noqa: F401
