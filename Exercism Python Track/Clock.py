"""
Instructions:

Implement a clock that handles times without dates.
You should be able to add and subtract minutes to it.
Two clocks that represent the same time should be equal to each other.
"""

class Clock(object):
    def __init__(self, hour, minute):
        self.minutes = (minute + (hour * 60)) % 1440

    def __repr__(self):
        return f"{str(self.minutes // 60).zfill(2)}:{str(self.minutes % 60).zfill(2)}"

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)
