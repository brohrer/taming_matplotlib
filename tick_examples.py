import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(1, 13, 500)
y = 1 + np.sinc(x - 7)

# Set axis limits.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.set_xlim(4, 10)
ax.set_ylim(-1, 3)
ax.set_xlabel("x-axis limits set at 4 and 10", fontsize=16)
ax.set_ylabel("y-axis limits set at -1 and 3", fontsize=16)
fig.savefig("images/axis_limits.png")

# Change to log scaling.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("log scale x-axis", fontsize=16)
ax.set_ylabel("log scale y-axis", fontsize=16)
fig.savefig("images/axis_log.png")

# Change tick direction.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.tick_params(axis="x", direction="in")
ax.tick_params(axis="y", direction="inout")
ax.set_xlabel("inward x-axis ticks", fontsize=16)
ax.set_ylabel("bi-directional y-axis ticks", fontsize=16)
fig.savefig("images/axis_tick_direction.png")

# Draw opposite ticks and labels.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.tick_params(bottom=False, top=True, left=True, right=True)
ax.tick_params(labelbottom=False, labeltop=True, labelleft=True, labelright=True)
ax.set_xlabel("x-axis ticks on top", fontsize=16)
ax.set_ylabel("y-axis ticks on both sides", fontsize=16)
fig.savefig("images/axis_tick_opposite.png")

# Style ticks.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.tick_params(axis="x", direction="in", length=16, width=2, color="turquoise")
ax.tick_params(axis="y", direction="in", length=6, width=4, color="orange")
ax.set_xlabel("long turquoise x-axis ticks", fontsize=16)
ax.set_ylabel("short orange y-axis ticks", fontsize=16)
fig.savefig("images/axis_tick_styled.png")

# Style tick labels.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.tick_params(axis="x", labelsize=18, labelrotation=-60, labelcolor="turquoise")
ax.tick_params(axis="y", labelsize=12, labelrotation=20, labelcolor="orange")
ax.set_xlabel("big turquoise x-axis ticks", fontsize=16)
ax.set_ylabel("small orange y-axis ticks", fontsize=16)
fig.savefig("images/axis_tick_label_styled.png")

# Minor ticks.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)

from matplotlib.ticker import AutoMinorLocator
x_minor_locator = AutoMinorLocator()
ax.xaxis.set_minor_locator(x_minor_locator)
y_minor_locator = AutoMinorLocator()
ax.yaxis.set_minor_locator(y_minor_locator)
ax.set_xlabel("minor x-axis ticks", fontsize=16)
ax.set_ylabel("minor y-axis ticks", fontsize=16)
fig.savefig("images/axis_tick_minor.png")

# Minor tick labels.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)

from matplotlib.ticker import AutoMinorLocator, FormatStrFormatter
formatter = FormatStrFormatter("%.3f")
x_minor_locator = AutoMinorLocator()
ax.xaxis.set_minor_locator(x_minor_locator)
y_minor_locator = AutoMinorLocator()
ax.yaxis.set_minor_locator(y_minor_locator)
ax.yaxis.set_minor_formatter(formatter)

ax.set_xlabel("minor x-axis ticks", fontsize=16)
ax.set_ylabel("minor y-axis ticks with labels", fontsize=16)
fig.savefig("images/axis_tick_labels_minor.png")

# Control your ticks.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)

from matplotlib.ticker import FixedLocator, FixedFormatter
x_formatter = FixedFormatter([
    "I like this spot",
    "and this",
    "and that",
    "but not this one."])
x_locator = FixedLocator([3, 7, 8.8, 12])
ax.xaxis.set_major_formatter(x_formatter)
ax.xaxis.set_major_locator(x_locator)

y_formatter = FixedFormatter(["-1e7", "111", "007", "xkcd"])
y_locator = FixedLocator([.85, 1.15, 1.28, 1.9])
ax.yaxis.set_major_formatter(y_formatter)
ax.yaxis.set_major_locator(y_locator)
ax.set_xlabel("custom x-axis ticks", fontsize=16)
ax.set_ylabel("custom y-axis ticks", fontsize=16)
fig.savefig("images/axis_tick_custom.png")

# incl dates

# Make a grid.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.grid(
    axis="x",
    color="green",
    alpha=.3,
    linewidth=2,
    linestyle=":")
ax.grid(
    axis="y",
    color="black",
    alpha=.5,
    linewidth=.5)
ax.set_xlabel("Dotted green x gridllines", fontsize=16)
ax.set_ylabel("Thin black y gridlines", fontsize=16)
fig.savefig("images/axis_tick_grid.png")
