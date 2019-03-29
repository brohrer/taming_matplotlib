import matplotlib
matplotlib.use("agg")

import matplotlib.pyplot as plt
import numpy as np


# Create the point data.
x = np.linspace(-1, 1)
y = x + np.random.normal(size=x.size)

# Vary the marker size.
fig = plt.figure()
ax = fig.gca()
ax.scatter(x, y, s=80)
fig.savefig("images/markers_large.png")

# Make markers different sizes
fig = plt.figure()
ax = fig.gca()
sizes = (np.random.sample(size=x.size) * 10) ** 2
ax.scatter(x, y, s=sizes)
fig.savefig("images/markers_sized.png")

# Vary the marker style.
fig = plt.figure()
ax = fig.gca()
ax.scatter(x, y, marker="v")
fig.savefig("images/markers_triangle.png")

# Make markers of different styles.
fig = plt.figure()
ax = fig.gca()
N = x.size // 3
ax.scatter(x[:N], y[:N], marker="o")
ax.scatter(x[N: 2 * N], y[N: 2 * N], marker="x")
ax.scatter(x[2 * N:], y[2 * N:], marker="s")
fig.savefig("images/markers_styled.png")

# Change the marker colors
fig = plt.figure()
ax = fig.gca()
ax.scatter(x, y, c="orange")
fig.savefig("images/markers_orange.png")

# Vary the marker colors.
fig = plt.figure()
ax = fig.gca()
ax.scatter(x, y, c=x - y)
fig.savefig("images/markers_colors.png")

# Create a lot of point data.
x = np.linspace(-1, 1, num=1e5)
y = x + np.random.normal(size=x.size)

# Make markers transparent.
fig = plt.figure()
ax = fig.gca()
ax.scatter(x, y, marker=".", alpha=.05, edgecolors="none")
fig.savefig("images/markers_transparent.png")
