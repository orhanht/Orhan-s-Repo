import numpy as np


class discreteRv:
    """
    Let q be a NumPy array of length n with q.sum() == 1.
    Suppose that q represents a probability mass function.
    We wish to generate a discrete random variable x such that P{x=i}=qi.
    In other words, x takes values in range(len(q)) and x = i with probability q[i].
    The standard (inverse transform) algorithm is as follows:
    Divide the unit interval [0,1] into n subintervals I0,I1,…,In−1 such that the length of Ii is qi.
    Draw a uniform random variable U on [0,1] and return the i such that U∈Ii.
    The probability of drawing i is the length of Ii, which is equal to qi.
    """
    def __init__(self, q):
        self.q = q

    def draw(self, k):
        cum_sum = np.cumsum(self.q)
        return cum_sum.searchsorted(np.random.uniform(0, 1, k))
