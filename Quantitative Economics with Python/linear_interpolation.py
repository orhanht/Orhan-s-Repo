# function approximation
def linapprox(f, a, b, n, x):
    """
    :param f: function
    :param a: scalar, Evaluation point
    :param b: scalar, Endpoint
    :param n: number of grid points in the interval
    :param x: scalar, with a <= x <= b
    :return: float, the interpolant evaluated at x
    """
    step = (b - a) / (n - 1)
    position = a
    while position <= x:
        position += step
    u, v = position - step, position
    return f(u) + (x - u) * (f(v) - f(u)) / (v - u)
