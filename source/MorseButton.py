"""

Author: Connor Fogarty
Last Modified: November 19th, 2019

Class for checking 'dits' and 'dahs' based on button hold length

"""


import time
from ParseInput import ParseInput
from tkinter import END as tk_END
import pyttsx3


class MorseButton:

	"""
	:param dit_length: the length of a dit (.) which is used when constructing the morse code string

	constructs a MorseButton object
	"""
	def __init__(self, dit_length, text_box):
		self.start_time = 0
		self.pressed = False
		self.dl = dit_length
		self.morse_string = ""
		self.pi = ParseInput(self)
		self.space_time = 0
		self.text_box = text_box
		self.engine = pyttsx3.init()


	"""
	:param event: event passed by button press function

	starts a timer used to calculate the length of the button press
	"""
	def button_pressed(self, event):
		self.pressed = True
		self.start_time = time.time()

		if self.space_time == 0: self.space_time = time.time()

		# if enough time has passed to add a space (2 dits)
		if time.time() - self.space_time >= 2 * self.dl:
			if self.morse_string[-1] == "w":
				self.space_time = 0
			else:
				self.morse_string += " "
		
		self.space_time = time.time()


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
			self.morse_string += "."
		else:
			self.morse_string += "-"

		self.text_box.delete('1.0', tk_END)
		self.text_box.insert(tk_END, self.pi.convert(self.morse_string))


	"""
	adds space to the morse_string
	"""
	def add_space(self):
		self.morse_string += "w"


	"""
	plays the audio of the morse_string
	"""
	def play_audio(self):
		print(self.pi.convert(self.morse_string))
		self.engine.say(self.pi.convert(self.morse_string))
		self.engine.runAndWait()


	"""
	clears the morse_string
	"""
	def clear_morse(self):
		self.morse_string = ""
		self.space_time = 0

		self.text_box.delete('1.0', tk_END)