import os
from morgan.settings import *   # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': os.environ.get('DB_HOST'),
    }
}

ALLOWED_HOSTS = ('dev.morgan-911.org', 'morgan-county.org',)

