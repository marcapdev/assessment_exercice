from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from sms import send_sms

import time

from api.models import User


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_sms(contacts: "list"):
    # send_sms(_("Validation"), _("message"), contacts, fail_silently=False)
    return f"Success SMS WITH {settings.SMS_PROVIDER} to {contacts}"


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_mail(contacts: "list"):
    # send_mail(_("Validation"), _("message"), "test_no_reply@gmail.com", [contacts])
    return f"Success MAIL WITH {settings.SMS_PROVIDER} to {contacts}"


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_sms_mockup(contacts: "list"):
    time.sleep(2)
    return f"Success MAIL MOCKUP WITH {settings.SMS_PROVIDER} to {contacts}"


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_mail_mockup(contacts: "list"):
    time.sleep(2)
    return f"Success MAIL MOCKUP WITH {settings.SMTP_PROVIDER} to {contacts}"
