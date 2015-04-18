from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from smugglers import settings

urlpatterns = patterns('',
                       url(r'^$', 'smugglers.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url('^markdown/', include('django_markdown.urls')),
                       url(r'^news/', include('news.urls')),
                       url(r'^send_email/', 'smugglers.views.send_email', name='send-email'),

                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)