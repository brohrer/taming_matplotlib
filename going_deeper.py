import matplotlib
matplotlib.use("agg")

from  matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.gca()

x = np.linspace(-6, 6, 500)
y = np.sinc(x)

ax.plot(x, y)

fig.savefig("curve.png")
