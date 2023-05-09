"""
Author: LESKERPIT Morgan レスカピット　モルガン
Keio ID: 8222300

COGNITIVE ROBOTICS ASSIGNMENT
"""
import time

import matplotlib.pyplot as plt
import numpy as np

# Study of the logistic map

def f_logistic(x: float, r: float) -> float:
    """

    :param x: X value at the step n
    :param r: r value
    :return: X value at the step n + 1
    """
    return r * x * (1 - x)


# Parameters
r = 2
U0 = 0.1
N = 1000

U_series = [U0]

# Plotting the logistic function
x_list = np.arange(0, 1, 0.01)
y_list = np.array([f_logistic(x, r) for x in x_list])

plt.plot(x_list, y_list)
plt.plot([x_list[0], x_list[-1]], [x_list[0], x_list[-1]], color='blue')

for n in range(0, N):
    Un1 = f_logistic(U_series[n], r)
    U_series.append(Un1)

x_showUSeriesStep = [U_series[0]]
y_showUSeriesStep = [U_series[0]]
for n in range(1, len(U_series)):
    x_showUSeriesStep.append(U_series[n-1])
    y_showUSeriesStep.append(U_series[n])

    x_showUSeriesStep.append(U_series[n])
    y_showUSeriesStep.append(U_series[n])


plt.plot(x_showUSeriesStep, y_showUSeriesStep, linestyle='-', marker='o')

plt.show()

def update(frame, frame_times):
    frame_times[frame] = time.perf_counter()
    y2= 1000*np.diff(frame_times)
    y2_avg = np.nanmean(y2)

    lineL.set_data(t[frame], y[frame])
    lineR.set_data(t[frame], y2)
    titL.set_text(f"N={frame}")
    titR.set_text(f"AVG = {y2_avg:.1f} ms ({1000/y2_avg:.1f} fps")

    rescale = False

    #...
