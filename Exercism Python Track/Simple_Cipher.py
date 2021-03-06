"""
Instructions:

Implement a simple shift cipher like Caesar and a more secure substitution cipher.
"""

import string
import random

letters = string.ascii_lowercase


class Cipher:

    def __init__(self, key=None):
        if key:
            self.key = key.lower()
        else:
            self.key = "".join(random.choice(letters) for i in range(100))

    def encode(self, text):
        encoded_text = ""
        for count, i in enumerate(text, 0):
            encoded_text += letters[(letters.find(self.key[count % len(self.key)]) +
                                    letters.find(i)) % 26]
        return encoded_text

    def decode(self, text):
        decoded_text = ""
        for count, i in enumerate(text, 0):
            decoded_text += letters[(- letters.find(self.key[count % len(self.key)]) +
                                    letters.find(i)) % 26]
        return decoded_text
