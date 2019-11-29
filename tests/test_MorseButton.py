import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import tkinter as tk
import time

from source import MorseButton
from source import ParseInput


class UnitTest(unittest.TestCase):

	def setUp(self):
		self.root = tk.Tk()
		self.morse_text = tk.Text(self.root, height=2, width=45)
		self.morse_text.pack()
		self.mb = MorseButton.MorseButton(.5, self.morse_text)

	def tearDown(self):
		del self.mb

	def test_MorseButton_created(self):
		attr_tuple = ("start_time", "pressed", "dl", "morse_string", "pi", "space_time", "text_box", "engine")
		for item in attr_tuple:
			self.assertEqual(item in self.mb.__dict__, True)

	def test_button_pressed(self):
		self.mb.button_pressed("event filler")
		self.assertAlmostEqual(round(self.mb.space_time, 3), round(time.time(), 3))

	def test_add_dit(self):
		self.mb.add_dit()
		self.assertEqual(self.mb.morse_string[-1], ".")

	def test_add_dah(self):
		self.mb.add_dah()
		self.assertEqual(self.mb.morse_string[-1], "-")

	def test_add_space(self):
		self.mb.add_space()
		self.assertEqual(self.mb.morse_string[-1], "w")
		self.assertEqual(self.mb.text_box.get("1.0"), "\n")

	def test_get_symbol_dah(self):
		self.mb.get_symbol(self.mb.dl * 2)
		self.assertEqual(self.mb.morse_string, "-")
		self.assertEqual(self.mb.text_box.get("1.0"), "T")

	def test_get_symbol_dah(self):
		self.mb.get_symbol(self.mb.dl * .5)
		self.assertEqual(self.mb.morse_string, ".")
		self.assertEqual(self.mb.text_box.get("1.0"), "E")

	def test_clear_morse(self):
		self.mb.clear_morse()
		self.assertEqual(self.mb.morse_string, "")
		self.assertEqual(self.mb.text_box.get("1.0"), "\n")

if __name__ == "__main__":
	unittest.main()