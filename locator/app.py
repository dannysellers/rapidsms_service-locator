from rapidsms.apps.base import AppBase
import models


class Counter(AppBase):

	def handle (self, msg):
		if msg.text == 'doctor':
			count = models.Entity.objects.filter(type = 'doctor').count()
			msg.respond("Doctors: {}".format(count))
			return True
		elif msg.text == 'market':
			count = models.Entity.objects.filter(type = 'market').count()
			msg.respond("Markets: {}".format(count))
			return True
		return False


# class Skeleton(AppBase):
# 	def filter (self, msg):
# 		""" Optionally abort further processing of the incoming message """
# 		pass
#
# 	def parse (self, msg):
# 		""" Modify message in a way that is globally useful """
# 		pass
#
# 	def handle (self, msg):
# 		""" Respond to the incoming message """
# 		pass
#
# 	def default (self, msg):
# 		""" Execute default action if no app returns True during handle phase """"
# 		pass
#
# 	def cleanup(self, msg):
# 		""" Perform cleanup after all handlers have run """
# 		pass
#
# 	def outgoing(self, msg):
# 		""" Handle outgoing message notifications """
# 		pass