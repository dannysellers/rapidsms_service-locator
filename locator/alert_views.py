from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt

from models import Entity
from rapidsms.models import Contact


@cache_control(no_cache = True)
def alert_overview(request):
	"""
	Overview page to show list of existing scheduled alerts
	"""
	context = RequestContext(request)
	context_dict = dict(contacts = Contact.objects.all())
	if request.method == 'GET':
		return render_to_response('locator/create_alert.html', context_dict, context)
	else:
		print(request.POST)
		# title = request.POST['title']
		# description = request.POST['description']

		return render_to_response('locator/create_alert.html', context_dict, context)


# @csrf_exempt
# def register_alert(request):
# 	pass