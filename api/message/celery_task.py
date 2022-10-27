from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from sms import send_sms


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_sms_task(contacts=None):
    if contacts:
        send_sms(_("Validation"), '+12065550100', contacts, fail_silently=False)
        return f"Success SMS WITH {settings.SMS_BACKEND} to {contacts}"
    else:
        return "Empty Contacts"


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_mail_task(contacts=None):
    if contacts:
        send_mail(_("Validation"), _("message"), "test_no_reply@gmail.com", contacts)
        return f"Success MAIL WITH {settings.EMAIL_BACKEND} to {contacts}"
    else:
        return "Empty Contacts"
