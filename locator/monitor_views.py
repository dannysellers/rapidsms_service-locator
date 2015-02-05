import json

from rapidsms.contrib.messagelog.models import Message
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# from models import LocationType, Entity


def query_count (request):
	"""
	Tallies queries, returns volume per day of week ( datetime.datetime.isoweekday() )
	:param request:
	:type request:
	:return: JSON
	:rtype: HttpResponse
	"""

	dict_data = {}
	data = "day,count\n"

	if request.method == 'GET':
		successful_messages = Message.objects.exclude(text = 'Sorry, RapidSMS could not understand your message.')
		# rudimentary filtering. if Message.objects[i].text = ^^, Message.objects.[i - 1] is unsuccessful
		# TODO: Track 'successful' vs 'unsuccessul' queries

		for message in successful_messages:
			_date = message.date.isoweekday()
			if _date not in dict_data:
				dict_data[_date] = 1
			else:
				dict_data[_date] += 1

		for key, value in dict_data.iteritems():
			data += "{},{}\n".format(key, value)

	return HttpResponse(data, content_type = 'application/json')


def report_page (request):
	"""
	View to load monitor.html template, which sets the stage for future
	AJAX queries / data viz
	"""
	context = RequestContext(request)
	context_dict = {}

	return render_to_response('locator/monitor.html', context_dict, context)