import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib import messages
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control

from service_locator.keys import MAPBOX_API_KEY, TEST_MAP_KEY
from forms import AddEntityForm
from models import LocationType, Entity


# Disable caching by browser
@cache_control(no_cache = True)
def entity_overview (request):
	context = RequestContext(request)
	queryset = Entity.objects.all()

	context_dict = dict(entity_list = list(queryset),
						headers = ['Name', 'Type', 'Location'],
						api_key = MAPBOX_API_KEY,
						map_key = TEST_MAP_KEY)
	return render_to_response('locator/entities.html', context_dict, context)


@csrf_exempt
def graph_entity (request, entity_id):
	"""
	Handles AJAX request for individual entity coordinates
	"""
	if request.method == 'GET':
		requested_entity = Entity.objects.get(location_id = entity_id)
	else:
		# Otherwise return some kind of home base?
		requested_entity = ''

	return HttpResponse(json.dumps(requested_entity.geojson), content_type = 'application/json')


@cache_control(no_cache = True)
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