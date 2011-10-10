from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# Site-wide 500 and 404 handler
handler500 = 'eio.views.server_error'
handler404 = 'eio.views.not_found'

urlpatterns = patterns('',
    # admin
    (r'^admin/', include(admin.site.urls)),

    # admin docs
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # admin tools
    (r'^admin_tools/', include('admin_tools.urls')),

    # blog
    (r'^blog/?', include('biblion.urls')),

    # home
    (r'', include('eio.home.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # Trick for Django to support static files (security hole: only for Dev environement! remove this on Prod!!!)
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
