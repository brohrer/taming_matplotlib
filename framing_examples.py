import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-6, 6, 500)
y = np.sinc(x)

# Manually set Axes by size and position.
fig = plt.figure()
ax = fig.add_axes((.2, .4, .4, .4))
ax.plot(x, y)
fig.savefig("images/framing_manual.png")

# Add multiple Axes.
fig = plt.figure()
ax1 = fig.add_axes((.1, .1, .35, .35))
ax1.plot(x, y)
ax2 = fig.add_axes((.1, .6, .35, .35))
ax2.plot(x, y)
ax3 = fig.add_axes((.55, .1, .35, .35))
ax3.plot(x, y)
ax4 = fig.add_axes((.55, .6, .35, .35))
ax4.plot(x, y)
ax5 = fig.add_axes((.35, .83, .08, .08))
ax5.plot(x, y)
ax6 = fig.add_axes((.75, .43, .23, .23))
ax6.plot(x, y)
ax7 = fig.add_axes((.35, -.15, .3, .3))
ax7.plot(x, y)
fig.savefig("images/framing_multiple.png")

# Fill figure with Axes.
fig = plt.figure()
ax1 = fig.add_axes((0, 0, 1, 1))
ax1.plot(x, y)
fig.savefig("images/framing_no_border.png")

# https://matplotlib.org/api/spines_api.html
# Turn axis spines off.
fig = plt.figure()
ax = fig.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.plot(x, y)
fig.savefig("images/framing_spines_off.png")

# Modify spine styles.
fig = plt.figure()
ax = fig.gca()
ax.spines['top'].set_color("orange")
ax.spines['left'].set_bounds(-.5, .5)
ax.spines['right'].set_linestyle("--")
ax.spines['bottom'].set_linewidth(6)
ax.spines['bottom'].set_capstyle("round")
ax.plot(x, y)
fig.savefig("images/framing_spines_styled.png")

# Move spines.
fig = plt.figure()
ax = fig.gca()
ax.spines['top'].set_position(("outward", 15))
ax.spines['bottom'].set_position(("data", 0))
ax.spines['left'].set_position(("axes", .3))
ax.spines['right'].set_position(("outward", -40))
ax.plot(x, y)
fig.savefig("images/framing_spines_moved.png")

# Change figure size.
fig = plt.figure(figsize=(4, 2))
ax = fig.gca()
ax.plot(x, y)
fig.savefig("images/framing_small_fig.png")

# Change figure resolution.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
fig.savefig("images/framing_lo_res_fig.png", dpi=15)

# Change the color of the plot area.
fig = plt.figure()
ax = fig.gca()
ax.set_facecolor("#e1ddbf")
ax.plot(x, y)
fig.savefig("images/framing_axes_bg_color.png")

# Change the color of the figure background.
fig = plt.figure(facecolor="#e1ddbf")
ax = fig.gca()
ax.plot(x, y)
fig.savefig("images/framing_fig_bg_color.png", facecolor=fig.get_facecolor())

# Change the color of the figure frame.
fig = plt.figure(linewidth=10, edgecolor="#04253a")
ax = fig.gca()
ax.plot(x, y)
fig.savefig("images/framing_fig_frame.png", edgecolor=fig.get_edgecolor())
