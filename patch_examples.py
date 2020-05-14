import matplotlib.patches as patches
import matplotlib.pyplot as plt


path = [
    [.1, .3],
    [.2, .9],
    [.8, .4],
]
fig = plt.figure()
ax = fig.gca()
ax.add_patch(patches.Polygon(path))
fig.savefig("triangle_patch.png", dpi=150)
plt.close()

path = [
    [.1, .3],
    [.2, .9],
    [.8, .4],
]
fig = plt.figure()
ax = fig.gca()
ax.add_patch(patches.Polygon(
  path,
  alpha=.7,
  edgecolor="darkblue",
  facecolor="red",
  hatch="+",
  joinstyle="miter",
  linestyle="--",
  linewidth=5,
))
fig.savefig("fancy_patch.png", dpi=150)
plt.close()
