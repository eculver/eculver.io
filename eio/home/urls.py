"""
URLs for home app.
Copyright (c) 2011 Evan Culver.
Author: Evan Culver <evan@eculver.io>
"""

from django.conf.urls.defaults import *

urlpatterns = patterns('eio.home.views',
    url(r'^/?$', 'home', name="home"),
)

