"""
Instructions:

Given the position of two queens on a chess board, indicate whether or not they are positioned so that they can attack each other.
In the game of chess, a queen can attack pieces which are on the same row, column, or diagonal.
A chessboard can be represented by an 8 by 8 array.
So if you're told the white queen is at (2, 3) and the black queen at (5, 6), then you'd know you've got a set-up like so:
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ W _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ B _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
You'd also be able to answer whether the queens can attack each other.
In this case, that answer would be yes, they can, because both pieces share a diagonal.
"""

class Queen:
    def __init__(self, row, column):
        if not 0 <= row <= 7 or not 0 <= column <= 7:
            raise ValueError("Coordinates are not valid!")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("They are at the same position!")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if self.row + self.column == another_queen.row + another_queen.column:
            return True
        if self.row - self.column == another_queen.row - another_queen.column:
            return True
        return False
