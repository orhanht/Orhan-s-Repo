import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


class Market:

    def __init__(self, ad, bd, az, bz, tax):
        """
        Set up scalar market parameters
        A linear demand curve Q=ad−bdp
        A linear supply curve Q=az+bz(p−t)
        """

        self.ad, self.bd, self.az, self.bz, self.tax = ad, bd, az, bz, tax
        if ad < az:
            raise ValueError("Insufficient demand!")

    def price(self):
        # Return equilibrium price
        return (self.ad - self.az + self.bz * self.tax) / (self.bd + self.bz)

    def quantity(self):
        # Return equilibrium quantity
        return self.ad - self.bd * self.price()

    def consumer_surplus(self):
        # Compute consumer surplus
        integrand = lambda x: (self.ad / self.bd) - (1 / self.bd) * x
        area, error = quad(integrand, 0, self.quantity())
        return area - self.price() * self.quantity()

    def producer_surplus(self):
        integrand = lambda x: -(self.az / self.bz) + (1 / self.bz) * x
        area, error = quad(integrand, 0, self.quantity())
        return (self.price() - self.tax) * self.quantity() - area

    def taxrev(self):
        return self.tax * self.quantity()

    def inverse_demand(self, x):
        return self.ad / self.bd - (1 / self.bd) * x

    def inverse_supply(self, x):
        return -(self.az / self.bz) + (1 / self.bz) * x + self.tax

    def inverse_supply_no_tax(self, x):
        return -(self.az / self.bz) + (1 / self.bz) * x


baseline_params = 15, .5, -2, .5, 3
m = Market(*baseline_params)

# print("Equilibrium price is ", m.price())
# print("Consumer surplus is", m.consumer_surplus())

q_max = m.quantity() * 2
q_grid = np.linspace(0.0, q_max, 100)
pd = m.inverse_demand(q_grid)
ps = m.inverse_supply(q_grid)
psno = m.inverse_supply_no_tax(q_grid)

fig, ax = plt.subplots()

ax.plot(q_grid, pd, lw=2, alpha=0.6, label="demand")
ax.plot(q_grid, ps, lw=2, alpha=0.6, label="supply")
ax.plot(q_grid, psno, lw=2, alpha=0.6, label="supply without tax")
ax.set_xlabel("quantity", fontsize=14)
ax.set_xlim(0, q_max)
ax.set_ylabel("price", fontsize=14)
ax.legend(loc="lower right", frameon=False, fontsize=14)
plt.show()


def deadw(m):
    """Computes deadweight loss for market m"""
    # Generate a market without taxes
    m_no_tax = Market(m.ad, m.bd, m.az, m.bz, 0)
    # Compare surplus, return the difference
    surp1 = m_no_tax.consumer_surplus() + m_no_tax.producer_surplus()
    surp2 = m.consumer_surplus() + m.producer_surplus() + m.taxrev()
    return surp1 - surp2


print(deadw(m))    # Show deadweight loss
