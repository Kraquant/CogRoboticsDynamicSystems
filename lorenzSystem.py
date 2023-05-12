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


def compute_lorenz_system(t0: float, v0: [float, float, float], s: float, r: float, b: float, h: float, n: int) -> []:
    """
    Compute a Lorenz system for a given set of parameters

    :param t0: Initial time
    :param v0: Initial vector
    :param s: Value for sigma
    :param r: Value for rho
    :param b: Value for beta
    :param h: Time step
    :param n: Number of calculated iterations
    :return: An array containing the time and the position at this time
    """
    t_list = [t0]
    v_list = [v0]

    def fl(t, y): return np.array(f_lorenz(y, s, r, b))

    for i in range(0, n):
        step_i1 = rk4(t_list[i], v_list[i], h, fl)

        t_list.append(step_i1[0])
        v_list.append(step_i1[1])

    return [t_list, v_list]


def diagram(t0: float,
            v0: [],
            s: float,
            r_i: float,
            r_f: float,
            m: int,
            b: float,
            h: float,
            n: int) -> [[float], [float]]:
    """

    :param t0: Initial time
    :param v0: Initial vector
    :param s: Value for sigma
    :param r_i: Initial value oh rho
    :param r_f: Final value of rho
    :param m: Number of values of rho to generate
    :param b: Value of beta
    :param h: Time step
    :param n: Number of computed iteration
    :return: On array containing the values of rho and an array containing the final values of the system
    """
    r_list = np.linspace(r_i, r_f, m)
    vn_list = [compute_lorenz_system(t0, v0, s, r, b, h, n)[1][-1] for r in r_list]
    return [r_list, vn_list]
