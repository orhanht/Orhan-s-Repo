"""
Instructions:

Given a number determine whether or not it is valid per the Luhn formula.
The Luhn algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers and Canadian Social Insurance Numbers.
The task is to check if a given string is valid.
"""

class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) < 2:
            return False
        if self.card_num.isdigit():
            count = 0
            for i in range(len(self.card_num[-2::-2])):
                if int(self.card_num[-2::-2][i]) > 4:
                    count += (2 * (int(self.card_num[-2::-2][i]))) - 9
                else:
                    count += 2 * (int(self.card_num[-2::-2][i]))
            for i in range(len(self.card_num[-1::-2])):
                count += int(self.card_num[-1::-2][i])
            if count % 10 == 0:
                return True
            else:
                return False
        else:
            return False
