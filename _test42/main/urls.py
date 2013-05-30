from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^requests/$', '_test42.main.views.request_log', name='request_log'),
    url(r'^request_delete/(?P<entry_id>[^/]+)/$', \
        '_test42.main.views.delete_request_log', name='request_log_delete'),
    url(r'^edit/(?P<profile_id>[^/]+)/$', '_test42.main.views.profile_edit', \
        name='profile_edit'),
    url(r'^$', '_test42.main.views.profile', name='profile'),
)
