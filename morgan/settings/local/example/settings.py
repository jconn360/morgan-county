from morgan.settings import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'dev.db'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'morgan',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#     }
# }

ROOT_URLCONF = 'morgan.settings.local.urls'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

