import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import ScalarMappable

fig = plt.figure()
ax = fig.gca()
img = np.array([[0, 1], [-1, 0]])
# custom_cmap = LinearSegmentedColormap.from_list(
#     "my_cmap",
#     ["red", "black", "white"])
custom_cmap = LinearSegmentedColormap.from_list(
    "my_cmap",
    [
        "xkcd:pumpkin orange",
        "xkcd:dusky blue",
        "xkcd:key lime",
        "xkcd:grape purple",
        "xkcd:really light blue",
        "xkcd:burnt siena",
        "xkcd:sunny yellow",
        "xkcd:purple brown",
        "xkcd:dried blood",
    ])
ax.imshow(img, cmap=custom_cmap, vmin=-1, vmax=1)
plt.colorbar(ScalarMappable(cmap=custom_cmap), orientation="horizontal")
plt.savefig(os.path.join("images", "plot_with_colormap.png"), dpi=300)
