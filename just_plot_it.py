import numpy as np
import matplotlib.pyplot as plt


x_curve = np.linspace(-2 * np.pi, 2 * np.pi, 500)
y_curve = np.sinc(x_curve)

plt.figure()
plt.plot(x_curve, y_curve)
plt.savefig("images/line_plot.png")
plt.show()

x_scatter = np.linspace(-1, 1)
y_scatter = x_scatter + np.random.normal(size=x_scatter.size)

plt.figure()
plt.scatter(x_scatter, y_scatter)
plt.savefig("images/scatter_plot.png")
plt.show()
