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


def compute_lorenz_system(t0, v0, s, r, b, h, n):
    t_list = [t0]
    v_list = [v0]

    def fl(t, y): return np.array(f_lorenz(y, s, r, b))

    for i in range(0, n):
        step_i1 = rk4(t_list[i], v_list[i], h, fl)

        t_list.append(step_i1[0])
        v_list.append(step_i1[1])

    return [t_list, v_list]