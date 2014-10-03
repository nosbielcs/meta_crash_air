# -*- coding: UTF-8 -*-
from django.conf.urls import patterns, include, url

from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^$', include(admin.site.urls)),
    #url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'potter.views.home', name='home'),
    # url(r'^potter/', include('potter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
