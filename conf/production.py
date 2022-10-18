# Import base environment configurations
from backend_assessment_exercice.settings import *

# Override base configurations

CELERY_DJANGO_SETTINGS = "conf.production"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.production')
