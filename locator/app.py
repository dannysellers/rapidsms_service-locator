from rapidsms.apps.base import AppBase

from models import *


class Counter(AppBase):

	def handle (self, msg):
		# To expose the identity (phone #, email, etc) for the sender, uncomment below
		# print("Identity:\t" + msg.connections[0].identity)
		if msg.text == 'doctor' or msg.text == 'doctors':
			count = Entity.objects.filter(type = 'doctor').count()
			msg.respond("Doctors: {}".format(count))
			return True
		elif msg.text == 'market' or msg.text == 'markets':
			count = Entity.objects.filter(type = 'food-distro').count()
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