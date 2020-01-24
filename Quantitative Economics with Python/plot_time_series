import matplotlib.pyplot as plt
import numpy as np


# plot 3 stationary time series with different coefficients
def plot_time_series(t=200, x=0.9):
    x_values = [0]
    for i in range(t):
        x_values.append(x_values[-1] * x + np.random.randn())
    plt.plot(x_values[1:], label=f"x = {x}")


plot_time_series(200, 0)
plot_time_series(200, .8)
plot_time_series(200, .98)
plt.legend()
plt.show()
