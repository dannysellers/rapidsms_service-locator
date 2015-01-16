from rapidsms.contrib.handlers import KeywordHandler, PatternHandler
# from django.utils.translation import ugettext as _  #, ugettext_lazy as __

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
	keyword = "help_test"
	# TODO: Add internationalization support

	def help (self):
		"""Called when the keyword matches but no text follows"""
		self.respond("Allowed commands are: (1), (2), and (3)")

	def handle (self, text):
		"""Called when the keyword matches and text follows

        :param text: The text that follows the keyword.  Any whitespace
             between the keyword and the text is not included.
        """
		text = text.strip().lower()
		self.respond("You asked for help with: {}".format(text))


class QueryHandler(PatternHandler):
	pattern = r'^$'
	""" All non-matching messages are silently ignored, to allow
	other apps or handlers to catch them. """

	def handle(self, *args):
		"""Called when the message matches the pattern. Any matching groups
        are passed to it.

        :param args: The matching groups from the regular expression.
        """
		pass