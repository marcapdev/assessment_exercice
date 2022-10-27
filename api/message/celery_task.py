from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from sms import send_sms


def send_sms_task(contacts: "list"):
    send_sms(_("Validation"), '+12065550100', contacts, fail_silently=False)
    # print(f"Success SMS WITH {settings.SMS_BACKEND} to {contacts}")
    return f"Success SMS WITH {settings.SMS_BACKEND} to {contacts}"


def send_mail_task(contacts: "list"):
    send_mail(_("Validation"), _("message"), "test_no_reply@gmail.com", contacts)
    # print(f"Success MAIL WITH {settings.EMAIL_BACKEND} to {contacts}")
    return f"Success MAIL WITH {settings.EMAIL_BACKEND} to {contacts}"
