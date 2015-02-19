from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.home', name='home'),
    url(r'^email/$', 'main.views.EmailCapture', name='EmailCapture'),
    url(r'^emails/?', 'main.views.AllEmails', name='all_emails'),
    url(r'^campaigns/?', 'main.views.campaigns', name='campaigns'),
    url(r'^campaign/(?P<id_num>\w{0,50})/$', 'main.views.campaign', name='campaign'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)