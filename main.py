"""
Author: LESKERPIT Morgan レスカピット　モルガン
Keio ID: 8222300

COGNITIVE ROBOTICS ASSIGNMENT
"""
import logisticFunction as lf
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
lSeries = lf.compute_Series(U0, r, N)

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

