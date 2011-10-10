"""
Generic, base views for eculver.io project.
Copyright (c) 2011 Evan Culver.
Author: Evan Culver <evan@eculver.io>
"""

from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response as r_t_r

# Shortcut used to always call render_to_response with a context_instance
render_to_response = lambda r, t, c: r_t_r(t, c, context_instance=RequestContext(r))

def server_error(request):
    "500 handler"
    context = {}
    return render_to_response(request, "500.html", context)

def not_found(request):
    "404 handler"
    context = {}
    return render_to_response(request, "404.html", context)
