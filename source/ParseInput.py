"""

Author: Connor Fogarty
Last Modified: November 29th, 2019

Class for parsing the "dits" and "dahs" inputted by the user and
converting them to a string of characters

"""

try:
	from NotValidMorse import NotValidMorse
except ModuleNotFoundError:
	from source import NotValidMorse
	NotValidMorse = NotValidMorse.NotValidMorse


class ParseInput:
    """
    :param mb: MorseButton object for use

    constructs a ParseInput object with an associated MorseButton
    object
    """
    def __init__(self, mb):
        self.mb = mb


    """
    :param str: the string containing . and - and w's which is converted to
    characters and words

    :returns: a string of characters

    function for converting the "dits" and "dahs" to chars and words
    """
    def convert(self, str):
        # splits the string into words
        word_list = str.split("w")
        final_str = ""

        # removes empty items from the word_list
        word_list = list(filter(None, word_list))

        for word in word_list:
            char_list = word.split(" ")
            char_str = ""

            for char in char_list:
                char_str += self.get_char(char)

            final_str += char_str + " "

        return final_str


    """
    :param str: a character to be parsed

    :returns: english character from morse

    get_char takes in a morse code pattern and
    returns the english representation of it
    """
    def get_char(self, str):
        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

        try:
            return list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(str)]
        except ValueError as x:
            self.mb.morse_string = self.mb.morse_string[:-1]
            raise NotValidMorse("That is not valid morse code") from None