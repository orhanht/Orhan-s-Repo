import matplotlib.pyplot as plt


class Chaos:
    """
    Chaotic dynamics in nonlinear systems
    One simple transition rule that can generate complex dynamics is the logistic map
    xt+1=rxt(1−xt),x0∈[0,1],r∈[0,4]
    """

    def __init__(self, x0, r):
        """Initialize with state x0 and parameter r"""
        self.x, self.r = x0, r

    def update(self):
        """Apply the map the update state"""
        self.x = self.r * self.x * (1 - self.x)

    def generate_sequence(self, n):
        """Generate and return a sequence"""
        path = []
        for i in range(n):
            path.append(self.x)
            self.update()
        return path


ch = Chaos(0.1, 4.0)
print(ch.generate_sequence(5))


ch = Chaos(0.1, 4.0)
ts_length = 250

fig, ax = plt.subplots()
ax.set_xlabel("$t$", fontsize=14)
ax.set_ylabel("$x_t$", fontsize=14)
x = ch.generate_sequence(ts_length)
ax.plot(range(ts_length), x, "bo-", alpha=0.5, lw=2)
plt.show()
