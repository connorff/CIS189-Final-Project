"""

Author: Connor Fogarty
Last Modified: November 27th, 2019

Class for parsing the "dits" and "dahs" inputted by the user and
converting them to a string of characters

"""


from NotValidMorse import NotValidMorse


class ParseInput:

    """
    :param str: the string containing . and - which is converted to
    characters

    :returns: a string of characters

    function for converting the "dits" and "dahs" to chars
    """
    def convert(self, str):
        char_list = str.split(" ")
        char_str = ""

        for char in char_list:
            char_str += self.get_char(char)

        return char_str


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
            raise NotValidMorse("That is not valid morse code") from None