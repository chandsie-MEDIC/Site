from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^MEDIC/admin/', include(admin.site.urls)),
    url(r'^MEDIC/', include('registry.urls')),
    
)
