import numpy as np
import matplotlib.pyplot as plt


f = lambda x: np.sin(4 * (x - 1/4)) + x + x**20 - 1
x = np.linspace(0, 1, 100)
fig, ax = plt.subplots()
ax.plot(x, f(x))
ax.axhline(ls="--", c="k")
plt.show()


# One of the most common algorithms for numerical root-finding is bisection.
def bisect(func, a, b, tol=10e-5):
    """
    Implements the bisection root finding algorithm, assuming that f is a
    real-valued function on [a, b] satisfying f(a) < 0 < f(b).
    """
    lower, upper = a, b
    while upper - lower > tol:
        middle_point = (upper + lower) / 2
        if func(middle_point) > 0:
            lower, upper = lower, middle_point  # if middle point is too big, take the first half of the interval as the new interval
        else:
            lower, upper = middle_point, upper  # vice versa
    return (lower + upper) / 2                  # return the mid-point when the interval is short enough


print(bisect(f, 0, 1))
