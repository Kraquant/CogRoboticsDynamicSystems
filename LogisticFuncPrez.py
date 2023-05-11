import logisticFunction as lf
import numpy as np
import matplotlib.pyplot as plt

#%%
# Data for the different plots
r = [1.0, 2.7, 3.5, 3.9]
U0 = [0.8, 0.8, 0.5, 0.8]
N = [1000, 1000, 1000, 1000]
lSeries = [lf.compute_series(U0[i], r[i], N[i]) for i in range(len(r))]

# Create the subplots for the different figures
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 12))

# Plotting the logistic function
x_list = np.arange(0, 1, 0.01)

plots = [ax1, ax2, ax3, ax4]
for i in range(len(lSeries)):
    plots[i].plot(lSeries[i][1], lSeries[i][2], linestyle='-', linewidth='0.6')
    plots[i].set_title(f'Logistic function for r={r[i]}, U0={U0[i]} and N={N[i]}')

    # Plotting the function y=x and the logistic function for a better visualisation
    y_list_i = np.array([lf.f_logistic(x, r[i]) for x in x_list])
    plots[i].plot(x_list, y_list_i, label='logistic function')
    plots[i].plot([x_list[0], x_list[-1]], [x_list[0], x_list[-1]], color='grey', label='y=x')

    plots[i].legend()

# Adjust the spacing between subplots
fig.tight_layout()

# Display the plots
plt.savefig('graphs/LogisticFunc.svg', format='svg')
plt.show()