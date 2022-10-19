from celery import shared_task
import time


def send_sms():
    time.sleep(10)
    return "Success SMS"


def send_mail():
    time.sleep(10)
    return "Success MAIL"


def send_sms_mockup():
    time.sleep(20)
    return "Success MOCKUP SMS"


def send_mail_mockup():
    time.sleep(20)
    return "Success MOCKUP MAIL"
