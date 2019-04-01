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
ax.set_xlabel("The x-axis label", fontsize=16)
ax.set_ylabel("The y-axis label", fontsize=16)
ax.set_title("The Title", fontsize=18)
fig.savefig("images/text_xy_labels_title.png")

# Add some text.
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.text(-5, .8, "Some text", fontsize=22)
fig.savefig("images/text_any_text.png")

# Align the text.
fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-2, 2])
ax.set_ylim([-1.4, 1.4])
left_pos = -1.8
right_pos = 1.8
top_pos = 1
bottom_pos = -1
center_pos = 0
baseline_pos = -.5
fontsize = 14
ax.scatter(left_pos, bottom_pos, marker=".", c="black")
ax.text(left_pos, bottom_pos, "left-bottom",
        fontsize=fontsize,
        horizontalalignment="left",
        verticalalignment="bottom")
ax.scatter(right_pos, bottom_pos, marker=".", c="black")
ax.text(right_pos, bottom_pos, "right-bottom",
        fontsize=fontsize,
        horizontalalignment="right",
        verticalalignment="bottom")
ax.scatter(left_pos, top_pos, marker=".", c="black")
ax.text(left_pos, top_pos, "left-top",
        fontsize=fontsize,
        horizontalalignment="left",
        verticalalignment="top")
ax.scatter(right_pos, top_pos, marker=".", c="black")
ax.text(right_pos, top_pos, "right-top",
        fontsize=fontsize,
        horizontalalignment="right",
        verticalalignment="top")
ax.scatter(center_pos, bottom_pos, marker=".", c="black")
ax.text(center_pos, bottom_pos, "center-bottom",
        fontsize=fontsize,
        horizontalalignment="center",
        verticalalignment="bottom")
ax.scatter(center_pos, top_pos, marker=".", c="black")
ax.text(center_pos, top_pos, "center-top",
        fontsize=fontsize,
        horizontalalignment="center",
        verticalalignment="top")
ax.scatter(right_pos, center_pos, marker=".", c="black")
ax.text(right_pos, center_pos, "right-center",
        fontsize=fontsize,
        horizontalalignment="right",
        verticalalignment="center")
ax.scatter(left_pos, center_pos, marker=".", c="black")
ax.text(left_pos, center_pos, "left-center",
        fontsize=fontsize,
        horizontalalignment="left",
        verticalalignment="center")
ax.scatter(right_pos, baseline_pos, marker=".", c="black")
ax.text(right_pos, baseline_pos, "right-baseline",
        fontsize=fontsize,
        horizontalalignment="right",
        verticalalignment="baseline")
ax.scatter(left_pos, baseline_pos, marker=".", c="black")
ax.text(left_pos, baseline_pos, "left-baseline",
        fontsize=fontsize,
        horizontalalignment="left",
        verticalalignment="baseline")
ax.scatter(center_pos, baseline_pos, marker=".", c="black")
ax.text(center_pos, baseline_pos, "center-baseline",
        fontsize=fontsize,
        horizontalalignment="center",
        verticalalignment="baseline")
ax.scatter(center_pos, center_pos, marker=".", c="black")
ax.text(center_pos, center_pos, "center-center",
        fontsize=fontsize,
        horizontalalignment="center",
        verticalalignment="center")
ax.set_title("Text alignment options", fontsize=18)
fig.savefig("images/text_alignment.png")

# Change the text formatting. 
fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
fontsize = 16
ax.text(-1, 1, 'fontsize=20', fontsize=20,
        horizontalalignment="center")
ax.text(-1, 0, 'fontstyle="italic"', fontstyle="italic",
        fontsize=fontsize,
        horizontalalignment="center")
ax.text(-1, -1, 'fontweight="bold"', fontweight="bold",
        fontsize=fontsize,
        horizontalalignment="center")
ax.text(1, -1, "rotation=15", rotation=15,
        fontsize=fontsize,
        horizontalalignment="center")
ax.text(1, 0, 'color="red"', color="red",
        fontsize=fontsize,
        horizontalalignment="center")
ax.text(1, 1, 'family="serif"', family="serif",
        fontsize=fontsize,
        horizontalalignment="center")
ax.set_title("A sampling of text styling options", fontsize=18)
fig.savefig("images/text_styles.png")

# Text box
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
ax.text(1, .7, "Text in a box",
        fontsize=20,
        bbox=dict(boxstyle = "square",
                  facecolor = "white"))
ax.set_title("A bounding box", fontsize=18)
fig.savefig("images/text_bbox.png")

# Annotation
fig = plt.figure()
ax = fig.gca()
ax.plot(x, y)
fontsize = 20
ax.annotate(
    '"-"',
    (2.4, np.sinc(2.4)),
    (3, .4),
    arrowprops=dict(arrowstyle = "-"),
    fontsize=fontsize,
)
ax.annotate(
    '"-|>"',
    (-2.4, np.sinc(2.4)),
    (-5, .3),
    arrowprops=dict(arrowstyle = "-|>"),
    fontsize=fontsize,
)
ax.annotate(
    '"<->"',
    (.5, np.sinc(.5)),
    (3, .6),
    arrowprops=dict(arrowstyle = "<->"),
    fontsize=fontsize,
)
ax.annotate(
    '"simple"',
    (0, 1),
    (-6, .7),
    arrowprops=dict(arrowstyle = "simple"),
    fontsize=fontsize,
)
ax.annotate(
    '"fancy"',
    (-.7, np.sinc(.7)),
    (-6, .55),
    arrowprops=dict(arrowstyle = "fancy"),
    fontsize=fontsize,
)
ax.set_title("A few arrowstyle options", fontsize=18)
fig.savefig("images/text_annotate.png")

# LaTeX equations. 
fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
matplotlib.rcParams['text.usetex'] = True
ax.text(
    0, 0,
    r"$f(x | \mu, \sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}" +
    r"e^{- \frac{(x - \mu)^2}{2\sigma^2}}$",
    horizontalalignment="center",
    fontsize=24)
matplotlib.rcParams['text.usetex'] = False
ax.set_title("So much math", fontsize=18)
fig.savefig("images/text_equation.png")

fig = plt.figure()
ax = fig.gca()
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
matplotlib.rcParams['text.usetex'] = True
ax.text(
    0, 0, r"$E=mc^2$",
    horizontalalignment="center",
    fontsize=32)
matplotlib.rcParams['text.usetex'] = False
ax.set_title("Some math", fontsize=18)
fig.savefig("images/text_equation_thumbnail.png")
matplotlib.rcParams['text.usetex'] = False

