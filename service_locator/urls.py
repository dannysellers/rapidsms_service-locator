from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.gis import admin
from locator import views as locator_views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # RapidSMS core URLs
    (r'^accounts/', include('rapidsms.urls.login_logout')),
    url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
    # RapidSMS contrib app URLs
    (r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    # (r'^locations/', include('rapidsms.contrib.locations.urls')),
    (r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    (r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    (r'^registration/', include('rapidsms.contrib.registration.urls')),

	# Custom URLs
	# TODO: Split URLs into app-specific file?
	# url(r'^define_map/', views.define_map, name = 'define_map'),
	url(r'^entities/', locator_views.entity_overview, name = 'entity_overview'),
	url(r'^add_entity/', locator_views.add_entity, name='add_entity'),
	url(r'^entity/(?P<entity_id>\d+)/$', locator_views.graph_entity, name='graph_entity'),
	url(r'^ajax_entities', locator_views.graph_entities, name='graph_multiple_entities'),

    # Third party URLs
    (r'^selectable/', include('selectable.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)