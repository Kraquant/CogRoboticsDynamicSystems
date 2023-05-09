import numpy as np
import matplotlib.pyplot as plt


def f_logistic(x: float, a: float) -> float:
    """

    :param x: X value at the step n
    :param a: r value
    :return: X value at the step n + 1
    """
    return a * x * (1 - x)


def f_logistic_recursive(x: float, a: float, n: int) -> float:
    """

    :param x:
    :param a:
    :param n:
    :return: for xi, return xi+n
    """
    if n == 0:
        return x
    else:
        return f_logistic_recursive(f_logistic(x, a), a, n - 1)


def bifurcation_diagram(u0: float, n: int, a_i: float, a_f: float, m: int) -> [float, float]:
    """

    :param u0: Initial value of the series
    :param n: Final value of U computed for a given a
    :param a_i: Initial value of the parameter a
    :param a_f: Final value of the parameter a
    :param m: Number of values of a
    :return: A list containing the values for a bifurcation diagram
    """
    a_list = np.linspace(a_i, a_f, m)
    un_list = [f_logistic_recursive(u0, a, n) for a in a_list]
    return [a_list, un_list]


def compute_series(u0, a, n):
    """

    :param u0: Initial value of the series
    :param a: Parameter a of the logistic function
    :param n: Final value of U computed
    :return: The first element is the series, the second and last are for plotting
    """
    u_series = [u0]

    for index in range(0, n):
        un1 = f_logistic(u_series[index], a)
        u_series.append(un1)

    x_show_u_series_step = [u_series[0]]
    y_show_u_series_step = [u_series[0]]
    for index in range(1, len(u_series)):
        x_show_u_series_step.append(u_series[index - 1])
        y_show_u_series_step.append(u_series[index])

        x_show_u_series_step.append(u_series[index])
        y_show_u_series_step.append(u_series[index])

    return [u_series, x_show_u_series_step, y_show_u_series_step]
