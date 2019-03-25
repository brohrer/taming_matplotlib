import matplotlib
matplotlib.use("agg")

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
print(fig)
ax = fig.gca()
print(ax)

x = np.linspace(-6, 6, 500)
y = np.sinc(x)

ax.plot(x, y)

fig.savefig("curve.png")
