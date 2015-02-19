from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'main.views.home', name='home'),
                       url(r'^campaigns/$', 'main.views.campaigns',
                           name='campaigns'),
                       url(r'^signup/$', 'main.views.email_form',
                           name='email_form'),
                       url(r'^giveaway/beer/$',
                           'main.views.beer_form', name='beer_form'),
                       url(r'^giveaway/language/$',
                           'main.views.language_form', name='language_form'),
                       url(r'^giveaway/shirt/$',
                           'main.views.shirt_form', name='shirt_form'),
                       url(r'^email/$', 'main.views.email_form',
                           name='email_form'),
                       url(r'^emails/?', 'main.views.all_emails',
                           name='all_emails'),
                       url(r'^thanks-for-your-input/?',
                           'main.views.thanks', name='thanks'),
                       url(r'^admin/', include(admin.site.urls)),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
