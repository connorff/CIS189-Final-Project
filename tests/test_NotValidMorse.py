import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import tkinter as tk
import time

from source import MorseButton
from source import ParseInput
from source import NotValidMorse


class UnitTest(unittest.TestCase):

	def setUp(self):
		self.root = tk.Tk()
		self.morse_text = tk.Text(self.root, height=2, width=45)
		self.morse_text.pack()
		self.mb = MorseButton.MorseButton(.5, self.morse_text)
		self.pi = ParseInput.ParseInput(self.mb)

	def tearDown(self):
		del self.mb
		del self.pi

	def test_get_char_raises(self):
		with self.assertRaises(NotValidMorse.NotValidMorse):
			self.pi.get_char(".......")

	def test_convert_raises(self):
		with self.assertRaises(NotValidMorse.NotValidMorse):
			self.pi.get_char("--- ... ------")

if __name__ == "__main__":
	unittest.main()