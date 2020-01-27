import numpy as np


# Approximation of pi using Monte Carlo
# We could use numba.njit to make it much faster (@njit(parallel=True) and prange instead of range)
def approximate_pi(n):
    number_of_coordinates_in = 0
    for i in range(n):
        coordinates = np.random.uniform(0, 1, 2)
        if coordinates[0] ** 2 + coordinates[1] ** 2 <= 1:
            number_of_coordinates_in += 1
    return 4 * number_of_coordinates_in / n
