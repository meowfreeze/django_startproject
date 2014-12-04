import json
import os

from unipath import Path


BASE_DIR = Path(__file__).ancestor(3)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Meow Freeze', 'meowfreeze@gmail.com'),
)

# location of secrets file
with open(BASE_DIR.child('secrets.json')) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = msg % var_name
        raise ImproperlyConfigured(error_msg)

# application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    # database migration
    'south',
)

LOCAL_APPS = (
    # project apps
    'core',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

# internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# additional locations of static files (compass project folder)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
     )
     
STATICFILES_DIRS = (
    (BASE_DIR.child('static')),
)

# additional locations of template files

TEMPLATE_DIRS = (
    (BASE_DIR.child('templates')),
)

# static files

STATIC_URL = '/assets/'

STATIC_ROOT = BASE_DIR.child('assets')

# media files

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.child('media')
