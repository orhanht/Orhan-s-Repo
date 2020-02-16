"""
Instructions:

So given a string with embedded newlines like:
9 8 7
5 3 2
6 6 7
your code should be able to spit out:
A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
A list of the columns, reading each column top-to-bottom while moving from left-to-right.
"""

class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.splitlines()
        self.rows = []
        for row in rows:
            self.rows.append([int(n) for n in row.split()])

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        columns = []
        for row in self.rows:
            columns.append(row[index - 1])
        return columns
