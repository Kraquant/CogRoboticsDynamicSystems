import numpy as np
import matplotlib.pyplot as plt
import lorenzSystem as ls

# Create the figure and subplots
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

n = 1000
rho_i = 0.001
rho_f = 30
sigma = 10
beta = 2.667

M = 200

dt = 0.01
t0 = 0

# Generate random vectors
initVectors = np.random.rand(100, 3)

#%%
lorenz = []
for v0 in initVectors:
    lorenz.append(ls.diagram(t0, v0, sigma, rho_i, rho_f, M, beta, dt, n))

    axes[0].plot(lorenz[-1][0], (np.array(lorenz[-1][1]).T)[0])
    axes[1].plot(lorenz[-1][0], (np.array(lorenz[-1][1]).T)[1])
    axes[2].plot(lorenz[-1][0], (np.array(lorenz[-1][1]).T)[2])

    print(v0)

#%%


# Plot the data in the subplots
axes[0].set_title('Projection over x')
axes[1].set_title('Projection over y')
axes[2].set_title('Projection over z')

# Set overall title and labels
fig.suptitle('Lorenz system for different initial values')
axes[0].set_xlabel('rho')
axes[1].set_xlabel('rho')
axes[2].set_xlabel('rho')
axes[0].set_ylabel(f'v n={n}')
axes[1].set_ylabel(f'v n={n}')
axes[2].set_ylabel(f'v n={n}')

plt.tight_layout()
plt.savefig('graphs/LorenzDiagram.svg', format='svg')
plt.show()
