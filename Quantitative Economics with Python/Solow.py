import matplotlib.pyplot as plt


class Solow:
    r"""
    Implements the Solow growth model with the update rule

        k_{t+1} = [(s z k^x_t) + (1 - d)k_t] /(1 + n)
    """

    def __init__(self,
                 n=0.05,    # population growth
                 s=0.25,    # savings rate
                 d=0.1,     # depreciation rate
                 x=0.3,     # share of labor
                 z=2.0,     # productivity
                 k=1.0):    # current capital stock

        self.n, self.s, self.d, self.x, self.z, self.k = n, s, d, x, z, k

    def h(self):
        # get rid of self to simplify notation
        n, s, d, x, z = self.n, self.s, self.d, self.x, self.z
        # apply update rule
        return (s * z * self.k ** x + (1 - d) * self.k) / (1 + n)

    def update(self):
        # update the current state
        self.k = self.h()

    def steady_state(self):
        # compute the steady state
        n, s, d, x, z = self.n, self.s, self.d, self.x, self.z
        # compute and return steady state
        return ((s * z) / (n + d)) ** (1 / (1 - x))

    def generate_sequence(self, t):
        # generate and return a time series of length t
        path = []
        for i in range(t):
            path.append(self.k)
            self.update()
        return path


s1 = Solow()
s2 = Solow(k=8.0)

T = 60
fig, ax = plt.subplots(figsize=(9, 6))

# plot the common steady state
ax.plot([s1.steady_state()] * T, "k-", label="steady state")

# plot the time series for each economy
for series in s1, s2:
    lb = f"capital series from initial state {series.k}"
    ax.plot(series.generate_sequence(T), "o-", lw=2, alpha=0.6, label=lb)

ax.set_xlabel("$k_{t+1}$", fontsize=14)
ax.set_ylabel("$k_t$", fontsize=14)
ax.legend()
plt.show()
