from django.db import models
# from django.contrib.gis.db import models
from django.utils.html import escape
from django.utils.text import slugify
# from django.utils.translation import ugettext as _  #, ugettext_lazy as __


class Point(models.Model):
	""" Lifted from rapidsms.contrib.locations.models.
	To be replaced with GeoDjango """

	latitude = models.DecimalField(max_digits = 13, decimal_places = 10)
	longitude = models.DecimalField(max_digits = 13, decimal_places = 10)

	def __unicode__ (self):
		return "{0}, {1}".format(self.latitude, self.longitude)

	def __repr__ (self):
		return '<{0}: {1}>'.format(type(self).__name__, self)


class LocationType(models.Model):
	""" Lifted from rapidsms.contrib.locations.models.
	To be replaced with GeoDjango """
	name = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True, primary_key = True)

	def __unicode__ (self):
		return self.name


class MapAreaManager(models.Manager):
	def create_map (self, name, x, y, height, width):
		slug = slugify(name)
		_location = Point.create(longitude = x, latitude = y)
		self.create(name = name, slug = slug, location = _location,
						   height = height, width = width)


class MapArea(models.Model):
	""" This class defines the map area for generating relative coordinates (i.e.
	the map box within which all beacons / points must be located) """
	name = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True, primary_key = True)
	location = models.ForeignKey(Point)
	# location = models.PointField(srid=4326)  # geodjango
	height = models.DecimalField(max_digits = 13, decimal_places = 10)
	width = models.DecimalField(max_digits = 13, decimal_places = 10)

	objects = MapAreaManager()

	def __unicode__(self):
		return u"Map: ({0}, {1})--{2} x {3}".format(self.location.longitude, self.location.latitude,
													self.width, self.height)


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


class Entity(models.Model):
	""" This class (eventually a base class) is the prototype for all
	entities (i.e. market, doctor) tracked by the system. """
	# TODO: Convert coordinates to built-in location
	location = models.ForeignKey(Point)
	# location = models.PointField(srid=4326)  # geodjango
	name = models.CharField(max_length = 100)
	slug = models.SlugField(primary_key = True, unique = True)
	type = models.ForeignKey(LocationType, related_name = "locations")

	objects = EntityManager()

	class Meta:
		verbose_name_plural = "entities"

	def __unicode__ (self):
		return u"{0}: {1}, {2}".format(self.name, self.location.latitude, self.location.longitude)

	@property
	def uid (self):
		return "{}:{}".format(self.type, self.pk)

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
		return unicode(self)