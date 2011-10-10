"""
A set of request processors that return dictionaries to be merged into a
template context. Each function takes the request object as its only parameter
and returns a dictionary to add to the context.

These are referenced from the setting TEMPLATE_CONTEXT_PROCESSORS and used by
RequestContext.
"""

from django.conf import settings

def default(request):
    "Returns context variables specific to totb views"

    context_extras = {
        "PROJECT_PREFIX" : settings.PROJECT_PREFIX,
        "WEBSITE_DOMAIN" : settings.WEBSITE_DOMAIN,
        "API_URL" : settings.API_URL,
        "MEDIA_URL": settings.MEDIA_URL,
        "STATIC_URL": settings.STATIC_URL,
        "STATIC_VERSION": settings.STATIC_VERSION,
    }

    return context_extras
