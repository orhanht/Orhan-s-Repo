"""
Instructions:

Write a robot simulator.
A robot factory's test facility needs a program to verify robot movements.
The robots have three possible movements:
turn right
turn left
advance
Robots are placed on a hypothetical infinite grid, facing a particular direction (north, east, south, or west) at a set of {x,y} coordinates, e.g., {3,8}, with coordinates increasing to the north and east.
The robot then receives a number of instructions, at which point the testing facility verifies the robot's new position, and in which direction it is pointing.
The letter-string "RAALAL" means:
Turn right
Advance twice
Turn left
Advance once
Turn left yet again
Say a robot starts at {7, 3} facing north. Then running this stream of instructions should leave it at {9, 4} facing west.
"""

# Globals
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot(object):
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)

    def move(self, instructions):
        for i in instructions:
            if i == "A":
                if self.direction == EAST:
                    self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
                elif self.direction == NORTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
                elif self.direction == WEST:
                    self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
                else:
                    self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
            elif i == "L":
                if self.direction == EAST:
                    self.direction = NORTH
                elif self.direction == NORTH:
                    self.direction = WEST
                elif self.direction == WEST:
                    self.direction = SOUTH
                else:
                    self.direction = EAST
            else:
                if self.direction == EAST:
                    self.direction = SOUTH
                elif self.direction == NORTH:
                    self.direction = EAST
                elif self.direction == WEST:
                    self.direction = NORTH
                else:
                    self.direction = WEST
