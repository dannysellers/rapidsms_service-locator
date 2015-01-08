# from models import Entity
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from service_locator.keys import MAPBOX_API_KEY


def define_map (request):
	context = RequestContext(request)
	context_dict = {'api_key': MAPBOX_API_KEY}

	return render_to_response('locator/define_map.html', context_dict, context)


def blank_view (request):
	return HttpResponse("This is a page!")


def entity_overview (request):
	return HttpResponse("Entities galore!")