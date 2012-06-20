from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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
    (r'^blog/', include('biblion.urls')),

    # flatpages
    (r'', include('eio.flatpages.urls')),

    # home
    (r'', include('eio.home.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
