import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "central_blood_bank.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import central_blood_bank.users.signals  # noqa: F401
