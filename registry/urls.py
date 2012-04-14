from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('registry.views',
    url(r'^register/$', 'register'),
    url(r'^user/(?P<username>\w+)/$', 'server_detail'),
    url(r'^user/$', 'detail'),
    url(r'^auth/$', 'server_auth'),
)

urlpatterns += patterns('',
    url(r'^$', direct_to_template, {'template': 'home.html'}),
    url(r'^success/$', direct_to_template, {'template': 'success.html'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
)
