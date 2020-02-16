from random import uniform


class ECDF:
    """
    The empirical cumulative distribution function (ecdf) corresponding to a sample {Xi}ni=1 is defined as
    Fn(x):=1n∑i=1n1{Xi≤x}(x∈R)(3)
    Here 1{Xi≤x} is an indicator function (one if Xi≤x and zero otherwise) and hence Fn(x) is the fraction of the
    sample that falls below x.
    """

    def __init__(self, samples):
        self.observations = samples

    def __call__(self, x):
        return sum([i <= x for i in self.observations]) / len(self.observations)


sample = [uniform(0, 1) for i in range(10)]
F = ECDF(sample)
print(F(0.5))

F.observations = [uniform(0, 1) for i in range(1000)]
print(F(0.5))
