from math import hypot
from models import Entity


def get_distance (entity, base):
	assert isinstance(entity, Entity)
	assert isinstance(base, Entity)
	return hypot(entity.location.longitude - base.location.longitude,
				 entity.location.latitude - base.location.latitude)


def get_closest (type, n, loc):
	""" Calculates distances between Entities of type 'type', and loc,
	returns the closest n objects """
	item_list = Entity.objects.filter(type = type)
	_list = []
	for item in item_list:
		assert isinstance(item, Entity)
		dist = get_distance(item, loc)
		_list.append({'entity': item, 'dist': dist})
	sorted_list = sorted(_list, key = lambda i: i['dist'])
	return sorted_list[0:n + 1]
