import logisticFunction as lf
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Create a figure and three subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Plot data on the first subplot
ax1.plot(x, y1, color='blue')
ax1.set_title('Sin(x)')

# Plot data on the second subplot
ax2.plot(x, y2, color='red')
ax2.set_title('Cos(x)')

# Plot data on the third subplot
ax3.plot(x, y3, color='green')
ax3.set_title('Tan(x)')

# Adjust the spacing between subplots
fig.tight_layout()

# Display the plots
plt.show()