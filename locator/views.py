from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django_tables2 import RequestConfig
from django.contrib import messages
from django.core.context_processors import csrf

from service_locator.keys import MAPBOX_API_KEY, TEST_MAP_KEY
from tables import EntityTable
from forms import *
from models import *


def define_map (request):
	# TODO: Settle define_map / add_entity division
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


def add_entity (request):
	context_dict = dict(api_key = MAPBOX_API_KEY,
						map_key = TEST_MAP_KEY,
						entity_types = tuple('{}'.format(i) for i in LocationType.objects.all()))

	if request.method == 'POST':
		form = AddEntityForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			name = cd['name']
			coords = cd['coordinates'].split(',')
			_type = LocationType.objects.get(name = cd['type'])

			Entity.objects.create_entity(x = coords[0], y = coords[1],
										 name = name, loc_type = _type)

			messages.add_message(request, messages.SUCCESS, "Entity added successfully.")
			return HttpResponseRedirect('/entities')
		else:
			messages.add_message(request, messages.ERROR, form.errors)
			# TODO: These messages aren't appearing until the user goes to /entities?
			return HttpResponseRedirect('/add_entity/')
	else:
		form = AddEntityForm()

	context_dict.update(csrf(request))
	context_dict['form'] = form

	return render_to_response('locator/define_map.html', context_dict)