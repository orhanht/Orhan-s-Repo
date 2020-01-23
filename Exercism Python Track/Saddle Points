"""
Instructions:

Detect saddle points in a matrix. It's called a "saddle point" because it is greater than or equal to every element in its row 
and less than or equal to every element in its column.
A matrix may have zero or more saddle points.
Your code should be able to provide the (possibly empty) list of all the saddle points for any given matrix.
The matrix can have a different number of rows and columns (Non square).

Note that you may find other definitions of matrix saddle points online, 
but the tests for this exercise follow the above unambiguous definition.
"""

import numpy as np


def saddle_points(matrix):
    mx = np.array(matrix)
    mx_transposed = mx.transpose()
    dicts_of_saddle_points = []
    for i in mx[1:]:
        if not len(i) == len(mx[0]):
            raise ValueError("Matrix is incomplete!")
    for i in range(len(mx)):
        for j in range(len(mx[i])):
            if mx[i][j] == max(mx[i]):
                if mx[i][j] == min(mx_transposed[j]):
                    dicts_of_saddle_points.append({"row": i + 1, "column": j + 1})
    return dicts_of_saddle_points
