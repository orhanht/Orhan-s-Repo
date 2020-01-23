"""
Instructions:

Manage robot factory settings.
When robots come off the factory floor, they have no name.
The first time you boot them up,
a random name is generated in the format of two uppercase letters followed by three digits, such as RX837 or BC811.
Every once in a while we need to reset a robot to its factory settings, which means that their name gets wiped.
The next time you ask, it will respond with a new random name.
The names must be random: they should not follow a predictable sequence. Random names means a risk of collisions.
Your solution must ensure that every existing robot has a unique name.
"""

import random
import string


class Robot(object):
    used_names = set()

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = self.assign_if_not_used()
        self.used_names.add(self.name)

    def assign_if_not_used(self):
        while True:
            new_name = self.gen_new_name()
            if new_name not in self.used_names:
                return new_name

    def gen_new_name(self):
        return random.choice(string.ascii_uppercase) + \
               random.choice(string.ascii_uppercase) + \
               str(random.randrange(0, 9)) + \
               str(random.randrange(0, 9)) + \
               str(random.randrange(0, 9))
