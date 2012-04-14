from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('registry.views',
#    url(r'^register/$', 'register'),
    
#    url(r'^user/(?P<username>\w+)/$', 'detail'),
    url(r'^user/$', 'detail'),
    url(r'^auth/$', 'auth'),
)

urlpatterns += patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
)
