from django.conf.urls import patterns, include, url

urlpatterns = patterns('registry.views',
    url(r'$', 'home'),
    url(r'register/$', 'register'),
    url(r'login/$', 'login'),
    url(r'auth/$', 'auth'),
)
