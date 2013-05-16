from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^requests/$', '_test42.main.views.request_log', name='request_log'),
    url(r'^$', '_test42.main.views.profile', name='profile')
)
