from celery import shared_task
import time


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_sms():
    time.sleep(10)
    return "Success SMS"


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_mail():
    time.sleep(10)
    return "Success MAIL"


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_sms_mockup():
    time.sleep(20)
    return "Success MOCKUP SMS"


@shared_task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 2, 'countdown': 2})
def send_mail_mockup():
    time.sleep(20)
    return "Success MOCKUP MAIL"
