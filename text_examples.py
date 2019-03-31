import matplotlib
matplotlib.use("agg")

import matplotlib.pyplot as plt
import numpy as np


# Create the curve data.
x = np.linspace(-6, 6, 500)
y = np.sinc(x)

# Add axis labels and a title.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.set_xlabel("The x-axis label")
ax.set_ylabel("The y-axis label")
ax.set_title("The Title")
fig.savefig("images/text_xy_labels_title.png")

# Add some text.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.text(-5, .8, "Text on a plot", fontsize=16)
fig.savefig("images/text_any_text.png")

# Align the text.
fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.scatter(-1, -1, marker=".", c="black")
ax.text(-1, -1, "right-top",
        horizontalalignment="right",
        verticalalignment="top")
ax.scatter(1, -1, marker=".", c="black")
ax.text(1, -1, "left-top",
        horizontalalignment="left",
        verticalalignment="top")
ax.scatter(-1, 1, marker=".", c="black")
ax.text(-1, 1, "right-bottom",
        horizontalalignment="right",
        verticalalignment="bottom")
ax.scatter(1, 1, marker=".", c="black")
ax.text(1, 1, "left-bottom",
        horizontalalignment="left",
        verticalalignment="bottom")
ax.scatter(0, -1, marker=".", c="black")
ax.text(0, -1, "horizcenter-top",
        horizontalalignment="center",
        verticalalignment="top")
ax.scatter(0, 1, marker=".", c="black")
ax.text(0, 1, "horizcenter-bottom",
        horizontalalignment="center",
        verticalalignment="bottom")
ax.scatter(1, 0, marker=".", c="black")
ax.text(1, 0, "left-vertcenter",
        horizontalalignment="left",
        verticalalignment="center")
ax.scatter(-1, 0, marker=".", c="black")
ax.text(-1, 0, "right-vertcenter",
        horizontalalignment="right",
        verticalalignment="center")
ax.scatter(1, .5, marker=".", c="black")
ax.text(1, .5, "left-baseline",
        horizontalalignment="left",
        verticalalignment="baseline")
ax.scatter(-1, .5, marker=".", c="black")
ax.text(-1, .5, "right-baseline",
        horizontalalignment="right",
        verticalalignment="baseline")
ax.scatter(0, .5, marker=".", c="black")
ax.text(0, .5, "center-baseline",
        horizontalalignment="center",
        verticalalignment="baseline")
ax.scatter(0, 0, marker=".", c="black")
ax.text(0, 0, "center-center",
        horizontalalignment="center",
        verticalalignment="center")
fig.savefig("images/text_alignment.png")

# Change the text formatting. 
fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.text(-1, 1, 'fontsize=16', fontsize=16,
        horizontalalignment="center")
ax.text(-1, 0, 'fontstyle="italic"', fontstyle="italic",
        horizontalalignment="center")
ax.text(-1, -1, 'fontweight="bold"', fontweight="bold",
        horizontalalignment="center")
ax.text(1, -1, "rotation=15", rotation=15,
        horizontalalignment="center")
ax.text(1, 0, 'color="red"', color="red",
        horizontalalignment="center")
ax.text(1, 1, 'family="serif"', family="serif",
        horizontalalignment="center")
fig.savefig("images/text_styles.png")

# Text box
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.text(2, .4, "Text in a box",
        bbox=dict(boxstyle = "square",
                  facecolor = "white"))
fig.savefig("images/text_bbox.png")

# Annotation
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.annotate(
    '"arrowstyle" = "-"',
    (2.4, np.sinc(2.4)),
    (3, .4),
    arrowprops=dict(arrowstyle = "-"),
)
ax.annotate(
    '"arrowstyle" = "-|>"',
    (-2.4, np.sinc(2.4)),
    (-5, .3),
    arrowprops=dict(arrowstyle = "-|>"),
)
ax.annotate(
    '"arrowstyle" = "<->"',
    (.5, np.sinc(.5)),
    (3, .6),
    arrowprops=dict(arrowstyle = "<->"),
)
ax.annotate(
    '"arrowstyle" = "simple"',
    (0, 1),
    (-6, .7),
    arrowprops=dict(arrowstyle = "simple"),
)
ax.annotate(
    '"arrowstyle" = "fancy"',
    (-.7, np.sinc(.7)),
    (-6, .55),
    arrowprops=dict(arrowstyle = "fancy"),
)
fig.savefig("images/text_annotate.png")

# LaTeX equations. 
matplotlib.rcParams['text.usetex'] = True
fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
# ax.text(0, 0, r"$y = \Sum{x^2 dx}_{i=0}^{n}$",
ax.text(
    0, 0,
    r"$f(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}" +
    r"e^{- \frac{(x - \mu)^2}{2\sigma^2}}$",
    horizontalalignment="center",
    fontsize=24)
fig.savefig("images/text_equation.png")

fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.text(
    0, 0, r"$E=mc^2$",
    horizontalalignment="center",
    fontsize=24)
fig.savefig("images/text_equation_thumbnail.png")
matplotlib.rcParams['text.usetex'] = False

