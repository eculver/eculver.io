# Django settings for production environment of eculver.io project.

import os

PROJECT_PATH = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'eio',                          # Or path to database file if using sqlite3.
        'USER': 'eio',                          # Not used with sqlite3.
        'PASSWORD': 'XxTdDWELQDV4DrnV',             # Not used with sqlite3.
        'HOST': '10.4.21.174',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                             # Set to empty string for default. Not used with sqlite3.
    }
}

# For versioning static files. Set during deploys to deploy timestamp
STATIC_VERSION = 'CURRENT_TIMESTAMP'

# Symlinked from CDN production origin export
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
STATIC_URL = 'http://cdn-prod.eio.distributed.io/static/%s' % STATIC_VERSION

# Memcached-based caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# Used in absolute URLs in JS and for Sitemaps root
WEBSITE_DOMAIN = 'http://eculver.io'

# Where to log on the local FS
LOGGING_FILENAME = '/var/log/eio/eio.log'
