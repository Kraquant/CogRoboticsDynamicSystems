import logisticFunction as lf
import numpy as np
import matplotlib.pyplot as plt

#U0 = np.linspace(0.000001, 0.8, 100)
U0 = [0.1, 0.1001]
n = 600
ri = 3.5
rf = 4

M = 1000

feigenbaum = [lf.bifurcation_diagram(u, n, ri, rf, M) for u in U0]
for i in range(len(feigenbaum)):
    plt.plot(feigenbaum[i][0], feigenbaum[i][1], label=f'u0={U0[i]}', linewidth='0.2')

plt.title('Feigenbaum diagram')
plt.xlabel("Values of r")
plt.ylabel(f'U for n={n}')
plt.legend()
plt.savefig('graphs/Feigenbaum diagram.svg', format='svg')
plt.show()
