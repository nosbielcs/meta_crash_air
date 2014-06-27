from django.conf.urls import patterns, include, url
from artigos.feeds import ArtigosRss
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'artigos.views.index'),
    url(r'^artigo/(?P<url>[^\.]+)','artigos.views.artigo'),
    url(r'^paginacao/(?P<pagina>[^\.]+)','artigos.views.index'),
    url(r'^form_pesquisa/$', 'artigos.views.form_pesquisa'),
    url(r'^pesquisa/$', 'artigos.views.pesquisa'),
    url(r'^contato','artigos.views.contato'),
    url(r'^rss/(?P<url>.*)', ArtigosRss()),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
