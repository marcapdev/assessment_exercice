# Import base environment configurations
from backend.settings import *
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
