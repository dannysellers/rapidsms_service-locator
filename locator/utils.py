from math import hypot, atan, degrees

from models import Entity


def trim_num (value, val_length=2):
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
	:return: hypotenuse plus unit of distance
	:rtype: str
	"""
	x = to_entity.location.longitude - from_entity.location.longitude
	y = to_entity.location.latitude - from_entity.location.latitude
	hypotenuse = hypot(x, y)
	# TODO: Confirm conversion of coordinates to km/m
	# divide hypotenuse by 1000 for km, and again by 1.6093 for miles?

	if hypotenuse <= 1:
		# If less than 1 km, scale up to meters
		hypotenuse *= 1000
		hypotenuse = str(trim_num(hypotenuse, trim_length) + " m")
	else:
		hypotenuse = str(trim_num(hypotenuse, trim_length) + " km")

	return hypotenuse


def get_angle (from_entity, to_entity):
	"""
	Calculates angle of direction from 'from_entity' to 'to_entity'
	:type from_entity: Entity
	:type to_entity: Entity
	:return: angle
	:rtype: float
	"""
	x = to_entity.location.longitude - from_entity.location.longitude
	y = to_entity.location.latitude - from_entity.location.latitude

	angle = trim_num(degrees(atan(x / y)))

	return angle


def get_closest (entity_list, n, loc):
	"""
	Get the 'n' items of 'entity_list' that are closest to 'loc'
	:param entity_list: List of Entities to consider
	:type entity_list: list
	:param n: Number of items to return
	:type n: int
	:param loc: Entity to get distances from
	:type loc: Entity
	:return: List of entities, ranked by distance
	"""
	_list = []
	for entity in entity_list:
		dist = get_distance(entity, loc, 4)
		_list.append({'entity': entity, 'dist': dist})
	sorted_list = sorted(_list, key = lambda i: i['dist'])
	if n == 1:
		# If just trying to get the closest entity, distance
		# is not returned---only a single object.
		# TODO: Merge get_closest and get_distance?
		return sorted_list[0]['entity']
	else:
		# If multiple entities are returned, distances are included.
		return sorted_list[0:n]
