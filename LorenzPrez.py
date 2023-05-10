import lorenzSystem as ls
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d import art3d

# Creating the colormap
cmap = mcolors.LinearSegmentedColormap.from_list('my_colormap', ['blue', 'red'])



# Initial values
sigma = 10
rho = 28
beta = 2.667

dt = 0.01
N = 10000
v0 = np.array([0., 1., 1.05])
t0 = 0

lorenzSystem = ls.compute_lorenz_system(t0, v0, sigma, rho, beta, dt, N)

ax = plt.figure(dpi=400).add_subplot(projection='3d')

ax.plot(*np.array(lorenzSystem[1]).T, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Lorenz Attractor for \u03C3={sigma}, \u03C1={rho}, \u03B2={beta}")

plt.show()