"""
Author: LESKERPIT Morgan レスカピット　モルガン
Keio ID: 8222300

COGNITIVE ROBOTICS ASSIGNMENT
"""
#%%
import logisticFunction as lf
import lorenzSystem as ls
import numpy as np
import matplotlib.pyplot as plt

plt.figure(dpi=400)

####################################################################
#################  STUDY OF THE LOGISTIC FUNCTION  #################
####################################################################
#%%
# Parameters to initialize
r = 3.9
U0 = 0.8
N = 1000
lSeries = lf.compute_series(U0, r, N)

# Plotting the logistic function
x_list = np.arange(0, 1, 0.01)
y_list = np.array([lf.f_logistic(x, r) for x in x_list])

plt.plot(x_list, y_list, label='logistic function')
plt.plot([x_list[0], x_list[-1]], [x_list[0], x_list[-1]], color='blue', label='y=x')
plt.plot(lSeries[1], lSeries[2], linestyle='-', marker='o')

# Plot settings
plt.title(f'Logistic function for r={r}, U0={U0} and N={N}')
plt.legend()
plt.show()

feigenbaum = lf.bifurcation_diagram(U0, 600, 1, 4, 20000)
plt.clf()
plt.plot(feigenbaum[0], feigenbaum[1])
plt.show()

####################################################################
###################  STUDY OF THE LORENZ SYSTEM  ###################
####################################################################
#%%

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
