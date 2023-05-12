import lorenzSystem as ls
import numpy as np
import matplotlib.pyplot as plt

# Initial values
sigma = 10
rho = 22
beta = 2.667

dt = 0.01
N = 10000
v0 = np.array([0., 1., 1.05])
t0 = 0

ax = plt.figure(dpi=400).add_subplot(projection='3d')

# %%
lorenzSystem = ls.compute_lorenz_system(t0, v0, sigma, rho, beta, dt, N)
lorenz_coords = np.array(lorenzSystem[1]).T

# %%
#Testing a different initial condition
v0_1 = np.array([0., 1.05, 1.05])
lorenzSystem_01 = ls.compute_lorenz_system(t0, v0_1, sigma, rho, beta, dt, N)
lorenz_coords_01 = np.array(lorenzSystem_01[1]).T
ax.plot(*lorenz_coords_01, linewidth='0.4', label=f'v0={v0_1}')

# %%
# ax.scatter(*lorenz_coords, c=np.linspace(0, 1, N + 1), cmap='viridis', linewidth=0.005)
ax.plot(*lorenz_coords, linewidth='0.4', label=f'v0={v0}')

# %%
# Fixed points
fixed_points = np.array([[0, 0, 0],
                         [np.sqrt(beta * (rho - 1.0)), np.sqrt(beta * (rho - 1.0)), rho - 1.0],
                         [-np.sqrt(beta * (rho - 1.0)), -np.sqrt(beta * (rho - 1.0)), rho - 1.0]])
ax.scatter(*fixed_points.T, c='red', s=50)



# %%
# Plotting and saving
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Lorenz Attractor for \u03C3={sigma}, \u03C1={rho}, \u03B2={beta}")
plt.legend()

plt.savefig('graphs/Lorenz.svg', format='svg')
plt.show()
