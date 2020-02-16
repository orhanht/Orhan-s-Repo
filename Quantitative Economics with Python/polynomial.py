# compute the polynomial with given coefficients
def p(x, coeffs):
  return sum([a * x ** i for i, a in enumerate(coeffs)])
