# Django settings for local development environment of eculver.io project.

import os

PROJECT_PATH = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'eio',                      # Or path to database file if using sqlite3.
        'USER': 'eio',                      # Not used with sqlite3.
        'PASSWORD': 'XxTdDWELQDV4DrnV',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INTERNAL_IPS = ('127.0.0.1',)

MEDIA_URL = '/media/'

STATIC_VERSION = 'dev'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static_build')

# URL prefix for static files.
STATIC_URL = '/static/'

# In-memory local caching.
CACHE_BACKEND = 'locmem:///'

# Used in absolute URLs in JS and for Sitemaps root
WEBSITE_DOMAIN = 'http://127.0.0.1:8000'

# Where to log on the local FS
LOGGING_FILENAME = 'eio.log'
