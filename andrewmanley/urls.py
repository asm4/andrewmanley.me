from django.conf.urls import patterns, include, url

from django.contrib import admin
from core import urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('core.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
