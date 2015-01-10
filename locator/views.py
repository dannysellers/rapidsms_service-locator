from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django_tables2 import RequestConfig

from service_locator.keys import MAPBOX_API_KEY, TEST_MAP_KEY
from tables import EntityTable
from models import *


def define_map (request):
	context = RequestContext(request)
	context_dict = {'api_key': MAPBOX_API_KEY,
					'map_key': TEST_MAP_KEY}

	return render_to_response('locator/define_map.html', context_dict, context)


def blank_view (request):
	return HttpResponse("This is a page!")


def entity_overview (request):
	queryset = Entity.objects.all()
	table = EntityTable(queryset)
	RequestConfig(request).configure(table)
	return render(request, "locator/entities.html", {'table': table})