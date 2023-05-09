import matplotlib.pyplot as plt
import numpy
import numpy as np


def f_lorenz(v, s, r, b):
    x = v[0]
    y = v[1]
    z = v[2]

    dx = s * (y - x)
    dy = x * (r - z) - y
    dz = x * y - b * z
    return [dx, dy, dz]


def rk4(tn, yn, h, f):
    k1 = f(tn, yn)
    k2 = f(tn + h / 2.0, yn + k1 / 2.0 * h)
    k3 = f(tn + h / 2.0, yn + k2 / 2.0 * h)
    k4 = f(tn + h, yn + k3 * h)

    yn1 = yn + h / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
    tn1 = tn + h

    return [tn1, yn1]


def compute_Lorenz_system(t0, v0, s, r, b, h, n):
    t_list = [t0]
    v_list = [v0]

    def fl(t, y): return np.array(f_lorenz(y, s, r, b))

    for i in range(0, n):
        step_i1 = rk4(t_list[i], v_list[i], h, fl)

        t_list.append(step_i1[0])
        v_list.append(step_i1[1])

    return [t_list, v_list]


# Initial values
sigma = 10
rho = 28
beta = 2.667

dt = 0.01
N = 10000
v0 = np.array([0., 1., 1.05])
t0 = 0

lorenzSystem = compute_Lorenz_system(t0, v0, sigma, rho, beta, dt, N)

ax = plt.figure(dpi=400).add_subplot(projection='3d')

ax.plot(*np.array(lorenzSystem[1]).T, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()