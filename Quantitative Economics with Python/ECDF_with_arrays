import numpy as np
import matplotlib.pyplot as plt


class ECDF:
    # I have done this before. Now re-doing it with arrays for efficiency
    """
    The empirical cumulative distribution function (ecdf) corresponding to a sample {Xi}ni=1 is defined as
    Fn(x):=1n∑i=1n1{Xi≤x}(x∈R)(3)
    Here 1{Xi≤x} is an indicator function (one if Xi≤x and zero otherwise) and hence Fn(x) is the fraction of the
    sample that falls below x.
    """

    def __init__(self, samples):
        # self.observations = samples
        self.observations = np.array(samples)

    def __call__(self, x):
        # return sum([i <= x for i in self.observations]) / len(self.observations)
        # return len(self.observations[self.observations <= x]) / len(self.observations)
        return np.mean(self.observations <= x)

    def plot(self, a=None, b=None):
        """
        :param a: float, optional. Lower endpoint of the interval
        :param b: float, optional. Upper endpoint of the interval
        :return: Plot of the interval
        """
        # choose a reasonable interval if [a, b] is not given
        if a is None:
            a = self.observations.min() - self.observations.std()
        if b is None:
            b = self.observations.max() + self.observations.std()

        x_vals = np.linspace(a, b, 100)
        f = np.vectorize(self.__call__)
        plt.plot(x_vals, f(x_vals))
        plt.show()


X = np.random.randn(1000)
F = ECDF(X)
F.plot()
