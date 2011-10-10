"""
Views for home app for eculver.io project.
Copyright (c) 2011 Evan Culver
Author: Evan Culver <e@eculver.io>
"""

import logging

from django.template import RequestContext
from django.shortcuts import render_to_response as r_t_r

# Shortcut used to always call render_to_response with a context_instance
render_to_response = lambda r, t, c: r_t_r(t, c, context_instance=RequestContext(r))


def home(request):
    "Site homepage"
    context = {}
    return render_to_response(request, "home/home.html", context)
