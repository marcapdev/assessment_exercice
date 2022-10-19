# Import base environment configurations
from backend_assessment_exercice.settings import *
import os

# Override base configurations
CELERY_BROKER_URL = "redis://redis:6379/0"
CELERY_RESULT_BACKEND = "redis://redis:6379/0"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.production')

SMTP_PROVIDER = "ACTUAL DATA"
SMS_PROVIDER = "ACTUAL DATA"
CONFIRMATION_MANAGER_CLASS = "ConfirmationManager"
