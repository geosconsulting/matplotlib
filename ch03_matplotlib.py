import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(6)
N = 16
x = np.linspace(0, 15, N)
# y = x + 1
y = np.logspace(0.1, 2, N)

z = np.geomspace(0.1, 2000, N)

plt.plot(x, y, 'o--')
plt.plot(x, -y, 'o-')
plt.plot(x, z, 'o-.')
# plt.title('y=x and y=-x')
# plt.axis('off')
plt.show()
