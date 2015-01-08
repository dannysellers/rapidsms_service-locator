from django.db import models
# from django.utils.translation import ugettext as _  #, ugettext_lazy as __


ENTITY_TYPES = (
	('0', 'doctor'),
	('1', 'market'),
)


# class EntityManager(models.Manager):
# 	def create_entity (self, lat, long, name, type):
# 		convert relative coordinates to absolute
# 		relative_lat = convert(lat)
# 		relative_long = convert(long)
# 		_entity = self.create(abs_latitude = lat, abs_longitude = long,
# 							  latitude = relative_lat, longitude = relative_long,
# 							  name = name, type = type)


class Entity(models.Model):
	""" This class (eventually a base class) is the prototype for all
	 entities (i.e. market, doctor) tracked by the system. """
	# TODO: Convert coordinates to built-in location
	latitude = models.DecimalField(max_digits = 13, decimal_places = 10)
	longitude = models.DecimalField(max_digits = 13, decimal_places = 10)
	abs_latitude = models.DecimalField(max_digits = 13, decimal_places = 10)
	abs_longitude = models.DecimalField(max_digits = 13, decimal_places = 10)
	name = models.CharField(primary_key = True, max_length = 100)
	type = models.CharField(choices = ENTITY_TYPES, max_length = 100)

	# objects = EntityManager()

	def __unicode__(self):
		# return _(u"{0}: {1}, {2}".format(self.type, self.latitude, self.longitude))
		return u"{0}: {1}, {2}".format(self.type, self.latitude, self.longitude)