import logisticFunction as lf
import numpy as np
import matplotlib.pyplot as plt

#U0 = [0.3, 0.8, 0.02, 0.00001, 0.0001]

U0 = np.linspace(0.000001, 0.8, 40)
n = 600
ai = 1
af = 4

M = 400

feigenbaum = [lf.bifurcation_diagram(u, n, ai, af, M) for u in U0]
for i in range(len(feigenbaum)):
    plt.plot(feigenbaum[i][0], feigenbaum[i][1], label=f'u0={U0[i]}', linewidth='0.2')

plt.title('Feigenbaum diagram')
plt.xlabel("Values of a")
plt.ylabel(f'U for n={n}')
plt.savefig('Feigenbaum diagram.pdf', format='pdf')
plt.show()
