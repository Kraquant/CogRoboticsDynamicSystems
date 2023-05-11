import numpy as np
import matplotlib.pyplot as plt


def f_logistic(x: float, r: float) -> float:
    """

    :param x: X value at the step n
    :param r: r value
    :return: X value at the step n + 1
    """
    return r * x * (1 - x)


def f_logistic_recursive(x: float, r: float, n: int) -> float:
    """

    :param x:
    :param r:
    :param n:
    :return: for xi, return xi+n
    """
    if n == 0:
        return x
    else:
        return f_logistic_recursive(f_logistic(x, r), r, n - 1)


def bifurcation_diagram(u0: float, n: int, r_i: float, r_f: float, m: int) -> [float, float]:
    """

    :param u0: Initial value of the series
    :param n: Final value of U computed for a given a
    :param r_i: Initial value of the parameter a
    :param r_f: Final value of the parameter a
    :param m: Number of values of a
    :return: A list containing the values for a bifurcation diagram
    """
    a_list = np.linspace(r_i, r_f, m)
    un_list = [f_logistic_recursive(u0, r, n) for r in a_list]
    return [a_list, un_list]


def compute_series(u0, r, n):
    """

    :param u0: Initial value of the series
    :param r: Parameter a of the logistic function
    :param n: Final value of U computed
    :return: The first element is the series, the second and last are for plotting
    """
    u_series = [u0]

    for index in range(0, n):
        un1 = f_logistic(u_series[index], r)
        u_series.append(un1)

    x_show_u_series_step = [u_series[0]]
    y_show_u_series_step = [u_series[0]]
    for index in range(1, len(u_series)):
        x_show_u_series_step.append(u_series[index - 1])
        y_show_u_series_step.append(u_series[index])

        x_show_u_series_step.append(u_series[index])
        y_show_u_series_step.append(u_series[index])

    return [u_series, x_show_u_series_step, y_show_u_series_step]
