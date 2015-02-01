from math import hypot, atan, degrees

from models import Entity


def trim_num (value, val_length):
	"""
	Receives `value`, truncates to length (used primarily for distances / angles)
	:param value: Value to truncate
	:type value: float
	:param val_length: Length to truncate after the decimal
	:type val_length: int
	:return: Trimmed number
	:rtype: str
	"""
	_length = int(val_length)
	_string = str(value).split('.')
	if len(_string[1]) == 1:
		_string[1] += '0'
	return _string[0] + '.' + _string[1][:_length]


def get_cardinal (angle):
	"""
	Get cardinal direction closest to angle.
	Ported from JS Gist at https://gist.github.com/basarat/4670200
	:param angle: Angle
	:type angle: str
	:return: Cardinal direction label
	:rtype: str
	"""
	cardinals = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
	# Get angle width of each cardinal's area
	arc_width = 360 / len(cardinals)

	# Ensure angle is between 0 and 360
	angle = float(angle) % 360

	# Detemine which sector the angle lies in
	# Subtract 1 to get the correct list index
	sector = int(round(angle / arc_width, 0)) - 1

	return cardinals[sector]


def get_distance (from_entity, to_entity, trim_length):
	"""
	Calculates hypotenuse and angle of direction from point 'base'
	 to point 'entity'.
	:param to_entity: Point to calculate direction to
	:type to_entity: Entity
	:param from_entity: Point to calculate from
	:type from_entity: Entity
	:param trim_length: Length to trim results after decimal
	:type trim_length: int
	:return: Hypotenuse and Direction
	:rtype: tuple
	"""
	assert isinstance(to_entity, Entity)
	assert isinstance(from_entity, Entity)
	x = to_entity.location.longitude - from_entity.location.longitude
	y = to_entity.location.latitude - from_entity.location.latitude
	hypotenuse = trim_num(hypot(x, y), trim_length)
	# TODO: Settle unit of distance
	# divide hypotenuse by 1000 for km, and again by 1.6093 for miles?
	direction = trim_num(degrees(atan(x / y)), trim_length)

	card_direction = get_cardinal(direction)

	return hypotenuse, direction, card_direction


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
