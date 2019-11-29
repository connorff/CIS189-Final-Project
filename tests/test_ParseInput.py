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
		self.pi = ParseInput.ParseInput(self.mb)

	def tearDown(self):
		del self.mb

	def test_convert_no_spaces(self):
		self.assertEqual(self.pi.convert(".... . .-.. .-.. ---"), "HELLO ")
		self.assertEqual(self.pi.convert("- . ... -"), "TEST ")

	def test_convert_with_spaces(self):
		self.assertEqual(self.pi.convert(".... . .-.. .-.. ---w- . ... -"), "HELLO TEST ")

	def test_get_char(self):
		self.assertEqual(self.pi.get_char("-.--"), "Y")
		self.assertEqual(self.pi.get_char("---"), "O")

if __name__ == "__main__":
	unittest.main()