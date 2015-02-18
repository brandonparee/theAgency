from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^makeAgency/$', 'main.views.makeAgency', name='makeAgency'),
    url(r'^makeAccount/$', 'main.views.makeAccount', name='makeAccount'),
    url(r'^makeGiveaway/$', 'main.views.makeGiveaway', name='makeGiveaway'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)