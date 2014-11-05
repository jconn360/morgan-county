import os
from morgan.settings import *   # pylint: disable=W0614,W0401

DEBUG = False
TEMPLATE_DEBUG = DEBUG

COMPRESS_OFFLINE = True

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

DEFAULT_FROM_EMAIL = 'Morgan County <{0}>'.format(os.environ.get('EMAIL_FROM'))
SERVER_EMAIL = os.environ.get('EMAIL_FROM')

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_HOST_PORT = 587
EMAIL_USE_TLS = True

