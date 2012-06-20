
from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^about/?$', direct_to_template, {'template': 'flatpages/about.html'}, name="flatpages_about"),
    url(r'^cv/?$', direct_to_template, {'template': 'flatpages/cv.html'}, name="flatpages_cv"),
)
