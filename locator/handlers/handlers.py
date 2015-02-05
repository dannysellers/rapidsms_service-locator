from rapidsms.contrib.handlers import KeywordHandler, PatternHandler
# from django.utils.translation import ugettext as _  #, ugettext_lazy as __
from locator.models import Entity
from locator.utils import get_distance

"""
ADD NEW HANDLERS TO RAPIDSMS_HANDLERS IN SETTINGS.PY
"""

"""
[Service] near [short code beacon location]
[Service] near [grid / coord position]
[Service] near [other entity]

Flows:
reg -- register phone / create a contact (used for permissions, etc)
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


class AtHandler(PatternHandler):
	"""
	Handler to process queries for [ENTITY] at or near any other [ENTITY].

	Returns the distance, relative angle, and cardinal direction from the
	first point to the second.
	"""
	# TODO: Track queries for aggregation
	pattern = r"^(.+)\s+(?:near|at)\s+(.+?)$"

	def handle (self, *args):
		try:
			from_pt = Entity.objects.get(slug__iexact = args[1])
		except Entity.DoesNotExist:
			return self.respond_error("Sorry, no point called '{}' could be found.".format(args[1]))

		try:
			to_pt = Entity.objects.get(slug__iexact = args[0])
		except Entity.DoesNotExist:
			return self.respond_error("Sorry, no point called '{}' could be found.".format(args[0]))

		distance, direction, card_direction = get_distance(from_pt, to_pt, 3)

		self.respond("A {4} called {0} can be found {1} km {2} degrees {5} from {3}.".format(
			to_pt, distance, direction, from_pt, to_pt.type.label, card_direction))


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
		self.respond("Try searching for [TERM] at [LOCATION], or send [LOCATION_TYPE] to get a count.")