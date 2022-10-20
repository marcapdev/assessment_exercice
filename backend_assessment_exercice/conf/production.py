# Import base environment configurations
from backend_assessment_exercice.settings import *
import os

# Override base configurations
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# get DB credentials from OS environment on docker
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_assessment_exercice.conf.production')

SMTP_PROVIDER = "SMTP ACTUAL DATA"
SMS_PROVIDER = "SMS ACTUAL DATA"
CONFIRMATION_MANAGER_CLASS = "ConfirmationManager"
