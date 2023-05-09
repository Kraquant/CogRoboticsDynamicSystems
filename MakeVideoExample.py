import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import numpy as np
plt.rcParams["figure.figsize"] = (12, 4)

N = 2**10
lwL = 2
lwR = 1
axRxlims = [0, N]
axRylims = [0, 160]

_t = np.linspace(0, N, N)
_y = (1+np.sin(5/N*2*np.pi*_t)) * (1+np.cos(2/N*2*np.pi*_t)) * \
     (0.9 * _t/N + 0.3) +\
    np.random.normal(loc=0.1, scale=0.01, size=N)
dframe = np.full(N+1, fill_value=np.nan, dtype=float)

t = np.tile(_t, (N, 1))
y = np.tile(_y, (N, 1))

for i in range(N):
    t[i, i+1:] = np.nan
    y[i, i+1:] = np.nan

# Plotting base graph
fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.set(xlabel="distance (m)", ylabel="Terrain height (m)")
ax.grid()
#ax.plot(t[-1], y[-1], lw=lwL)

xlist = []
ylist = []


l, = plt.plot([], [], 'k-')
metadata = dict(title='Movie', artist='Leskerpit Morgan')
writer = PillowWriter(fps=15, metadata=metadata)

with writer.saving(fig, "Fonction_Bizarre.gif", 100):
    for i in range(len(t[-1])):
        xlist.append(t[-1][i])
        ylist.append(y[-1][i])

        l.set_data(xlist, ylist)
        print(str(i) + "/" + str(N))
        writer.grab_frame()