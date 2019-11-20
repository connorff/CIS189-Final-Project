"""

Author: Connor Fogarty
Last Modified: November 19th, 2019

Class for checking 'dits' and 'dahs' based on button hold length

"""


import time


class MorseButton:

	"""
	:param dit_length: the length of a dit (.) which is used when constructing the morse code string

	constructs a MorseButton object
	"""
	def __init__(self, dit_length):
		self.start_time = 0
		self.pressed = False
		self.dl = dit_length


	"""
	:param event: event passed by button press function

	starts a timer used to calculate the length of the button press
	"""
	def button_pressed(self, event):
		self.pressed = True
		self.start_time = time.time()


	"""
	:param event: event passed by button release function

	:returns: the value of the button press length

	measures the elapsed time of the button press
	"""
	def button_release(self, event):
		elapsed_time = time.time() - self.start_time
		self.pressed = False
		return self.get_symbol(elapsed_time)


	"""
	:param hold_time: amount of time the button was held down

	:returns: 1 for dit (.), 2 for dah(-)

	uses the time passed in to return the appropriate morse code unit
	"""
	def get_symbol(self, hold_time):
		if hold_time <= self.dl:
			return 1
		else:
			return 2
