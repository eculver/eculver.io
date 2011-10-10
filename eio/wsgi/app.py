import os, sys, site

# Virtualenv!
site.addsitedir('/var/www/.virtualenvs/totb/lib/python2.6/site-packages')

# Is this the right way to do this?
sys.path.append('/var/www/totb')

os.environ['DJANGO_SETTINGS_MODULE'] = 'totb.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
