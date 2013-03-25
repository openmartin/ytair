from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'check_in.views.home', name='home'),
#    url(r'^home', 'check_in.views.home', name='home'),
#    url(r'^query', 'check_in.views.query', name='query'),
#    url(r'^check', 'check_in.views.check', name='check'),
#    url(r'^cancel', 'check_in.views.cancel', name='cancel'),
    
    # url(r'^check_in/', include('check_in.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
