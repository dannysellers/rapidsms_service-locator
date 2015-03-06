import json
from utils import trim_num
from rapidsms.contrib.messagelog.models import Message
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# from datetime import date

# from models import LocationType, Entity


def query_count (request):
	"""
	Tallies queries, returns volume per day of week ( datetime.datetime.isoweekday() )
	:param request:
	:type request:
	:return: CSV
	:rtype: HttpResponse
	"""

	dict_data = {}
	# data = "day,percent\n"
	returned_data = dict(labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
				datasets = [])

	if request.method == 'GET':
		successful_messages = Message.objects.exclude(text = 'Sorry, RapidSMS could not understand your message.')
		# rudimentary filtering. if Message.objects[i].text = ^^, Message.objects[i - 1] is unsuccessful
		# TODO: Track 'successful' vs 'unsuccessul' queries

		# Data keys for Chartjs, per data-set
		dict_data['label'] = 'Successful* queries'
		dict_data['fillColor'] = 'rgba(220,220,220,0.5)'
		dict_data['strokeColor'] = 'rgba(220,220,220,0.8)'
		dict_data['highlightFill'] = 'rgba(220,220,220,0.75)'
		dict_data['highlightStroke'] = 'rgba(220,220,220,1)'

		count_dict = {}
		_data = []

		for message in successful_messages:
			# isoweekday: 1 = Monday, 7 = Sunday
			# _date = date.strftime(message.date, '%A')
			_date = message.date.weekday()
			if _date not in count_dict:
				count_dict[_date] = 1
			else:
				count_dict[_date] += 1

		for value in count_dict.values():
			# Return value as percentage
			value = (value / float(len(successful_messages))) * 100
			_data.append(trim_num(value))

		dict_data['data'] = _data
		returned_data['datasets'].append(dict_data)

	return HttpResponse(json.dumps(returned_data), content_type = 'application/json')


def report_page (request):
	"""
	View to load monitor.html template, which sets the stage for future
	AJAX queries / data viz
	"""
	context = RequestContext(request)
	context_dict = {}

	return render_to_response('locator/monitor.html', context_dict, context)