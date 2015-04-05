from django.conf.urls import patterns, url

urlpatterns = patterns('locator.views',
   url(r'^$', 'dashboard', name = 'dashboard'),
   url(r'^entities/$', 'entity_overview', name = 'entity_overview'),
   url(r'^add_entity/$', 'add_entity', name = 'add_entity'),
   url(r'^map_entities/', 'graph_entities', name = 'map_entities')
)

urlpatterns += patterns('locator.monitor_views',
	url(r'^reports/$', 'report_page', name = 'report_page'),
	url(r'^monitor/$', 'query_count', name = 'query_count'),
)

urlpatterns += patterns('locator.alert_views',
	url(r'^alert/$', 'alert_overview', name = 'alert_overview'),
)