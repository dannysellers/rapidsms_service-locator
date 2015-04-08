from rapidsms.contrib.handlers import KeywordHandler, PatternHandler
# from django.utils.translation import ugettext as _  #, ugettext_lazy as __
from locator.models import Entity
from locator import utils

"""
ADD NEW HANDLERS TO RAPIDSMS_HANDLERS IN SETTINGS.PY
"""

"""
[Service] near [short code beacon location]
[Service] near [grid / coord position]
[Service] near [other entity]

Flows:
new [Service] -- create new entity
del [Service ID] -- remove existing entity?
"""


class HelpHandler(KeywordHandler):
	"""
	Handler to process requests for help.
	"""
	keyword = "help"
	# TODO: Add internationalization support

	def help (self):
		"""Called when the keyword matches but no text follows"""
		self.respond("Try searching for [TERM] near [BEACON], or send [LOCATION_TYPE] to get a count.")

	def handle (self, text):
		"""Called when the keyword matches and text follows

        :param text: The text that follows the keyword.  Any whitespace
             between the keyword and the text is not included.
        """
		text = text.strip().lower()
		self.respond("You asked for help with: {}".format(text))
		return True


class AtHandler(PatternHandler):
	"""
	Handler to process queries for Entity of specified type at or near any other Entity.

	Returns the distance, relative angle, and cardinal direction from the
	first point to the second.
	"""
	# TODO: Track queries for aggregation
	pattern = r"^(.+)\s+(?:near|at)\s+(.+?)$"

	def handle (self, *args):
		try:
			# Retrieve all points of type args[0]
			to_type_list = Entity.objects.filter(type = args[0])
		except Entity.DoesNotExist:
			return self.respond_error("Sorry, no points of type '{}' could be found.".format(args[1]))

		try:
			from_pt = Entity.objects.get(slug__iexact = args[1])
		except Entity.DoesNotExist:
			return self.respond_error("Sorry, no point called '{}' could be found.".format(args[0]))

		# Get the point closest to args[1]
		to_pt = utils.get_closest(to_type_list, from_pt)

		distance = utils.get_distance(from_pt, to_pt)
		diff_x, diff_y, angle = utils.get_angle(from_pt, to_pt)

		card_direction = utils.get_cardinal(angle)

		self.respond("A {0} called {1} can be found {2}, {3} ({4} at {5}) from {6}.".format(
			to_pt, to_pt.type.label, diff_x, diff_y, distance, card_direction, from_pt))
		return True


class QueryHandler(PatternHandler):
	"""
	Default handler to catch messages not processed by other handlers in this file.
	"""
	pattern = r'^$'
	""" All non-matching messages are silently ignored, to allow
	other apps or handlers to catch them. """

	def handle (self, *args):
		"""Called when the message matches the pattern. Any matching groups
        are passed to it.

        :param args: The matching groups from the regular expression.
        """
		self.respond("Try searching for [TERM] at/near [LOCATION], or send [LOCATION_TYPE] to get a count.")
		return True