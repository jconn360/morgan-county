
from morgan.settings import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'morgan',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

