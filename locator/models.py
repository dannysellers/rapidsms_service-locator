from django.db import models
# from django.contrib.gis.db import models
from django.utils.html import escape
from django.utils.text import slugify
from django.utils.translation import ugettext as _, ugettext_lazy as __
from audit_log.models import AuthStampedModel
from audit_log.models.managers import AuditLog


class Point(AuthStampedModel):
	""" Lifted from rapidsms.contrib.locations.models.
	To be replaced with GeoDjango.

	This model represents an anonymous point on the globe.
	"""

	class Meta:
		verbose_name = __("Point")
		verbose_name_plural = __("Points")

	latitude = models.DecimalField(max_digits = 13, decimal_places = 10)
	longitude = models.DecimalField(max_digits = 13, decimal_places = 10)

	audit_log = AuditLog()

	def __unicode__ (self):
		return _(u"{0}, {1}".format(self.latitude, self.longitude))

	def __repr__ (self):
		return '<{0}: {1}>'.format(type(self).__name__, self)

	@property
	def coords (self):
		""" Dict for use with AJAX responses """
		# TODO: JSON response requires these be floats. Any reason to leave them as Decimal?
		return dict(longitude = float(self.longitude), latitude = float(self.latitude))


class LocationType(AuthStampedModel):
	""" Lifted from rapidsms.contrib.locations.models.
	To be replaced with GeoDjango.

	This model represents the 'type' of Location, as an option for a
	simpler way of having a location hierarchy without having different
	classes for each location type (as is supported by the generic
	relation to parent).
	"""

	class Meta:
		verbose_name = __("Location Type")
		verbose_name_plural = __("Location Types")

	name = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True, primary_key = True)

	audit_log = AuditLog()

	def __unicode__ (self):
		return _(u"{}".format(self.name))

	@property
	def label (self):
		return unicode(self)


class MapAreaManager(models.Manager):
	def create_map (self, name, x, y, height, width):
		slug = slugify(name)
		_location = Point.create(longitude = x, latitude = y)
		self.create(name = name, slug = slug, location = _location,
					height = height, width = width)


class MapArea(AuthStampedModel):
	""" This class defines the map area for generating relative coordinates (i.e.
	the map box within which all beacons / points must be located) """
	name = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True, primary_key = True)
	location = models.ForeignKey(Point)
	# location = models.PointField(srid=4326)  # geodjango
	height = models.DecimalField(max_digits = 13, decimal_places = 10)
	width = models.DecimalField(max_digits = 13, decimal_places = 10)

	objects = MapAreaManager()
	audit_log = AuditLog()

	def __unicode__ (self):
		return _(u"Map: ({0}, {1})--{2} x {3}".format(self.location.longitude, self.location.latitude,
													  self.width, self.height))


class EntityManager(models.Manager):
	def create_entity (self, x, y, name, loc_type):
		# TODO: Settle issue of relative/absolute coordinates
		_location = Point.objects.get_or_create(longitude = x, latitude = y)[0]
		_slug = slugify(name)
		_type = LocationType.objects.get(name = loc_type)
		if not _type:
			# TODO: Necessary? Only the name is passed from the form/view
			_type = LocationType.objects.get_or_create(slug = loc_type)[0]

		self.create(location = _location, name = name,
					slug = _slug, type = _type)


class Entity(AuthStampedModel):
	""" This class (eventually a base class) is the prototype for all
	entities (i.e. market, doctor) tracked by the system.

	Directions may be calculated from any point to any point.

	Rather than try and create a short-code system for identifying beacons (i.e. 'AXX101L'),
	a semantic identifier, such as local flora/fauna or national landmarks, might be more
	useful and memorable. """

	# TODO: Any reason to impose directions being calculated only from Entities with type Beacon?

	class Meta:
		verbose_name = __("Entity")
		verbose_name_plural = __("Entities")

	location = models.ForeignKey(Point)
	name = models.CharField(max_length = 100)
	slug = models.SlugField(primary_key = True, unique = True)
	type = models.ForeignKey(LocationType, related_name = "locations")

	objects = EntityManager()
	audit_log = AuditLog()

	def __unicode__ (self):
		return getattr(self, "name", "#{}".format(self.pk))

	# return _(u"{0}: {1}, {2}".format(self.name, self.location.latitude, self.location.longitude))

	@property
	def uid (self):
		return "{}:{}".format(self.type, self.pk)

	@property
	def as_html (self):
		"""
		Return HTML fragment for embedding in a map.
		"""
		return escape(self.slug)

	@property
	def label (self):
		"""
		Return the caption for this Entity, to be embedded in the map.
		"""
		return unicode(self.name)

	@property
	def coords (self):
		# return [coord for coord in self.location.coords.values()]
		return self.location.coords

	@property
	def geojson (self):
		"""
		Processes Entity attributes, returns (minimal) GeoJSON obj
		:return: GeoJSON Obj
		:rtype: GeoJSON
		"""
		_type = "Point"
		_coords = [coord for coord in self.location.coords.values()]

		geodict = dict(type = _type, coordinates = _coords)

		return geodict