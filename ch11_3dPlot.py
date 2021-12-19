import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 30, 1000)
x = np.sin(z)
y = np.cos(z)

# ax.plot3D(x, y, z, 'red')

# y = np.random.random(100)
# x = np.random.random(100)
# z = np.random.random(100)
# ax.scatter3D(x,y,z, cmap='cool')

x = y = z = np.arange(-0.1, 1, 0.2)
X, Y, Z = np.meshgrid(x, y, z)
u = np.cos(np.pi * X) * np.sin(np.pi * Y) * np.sin(np.pi * Z)
v = -np.sin(np.pi * X) * np.cos(np.pi * Y) * np.sin(np.pi * Z)
w = np.sin(np.pi * X) * np.sin(np.pi * Y) * np.cos(np.pi * Z)

ax.quiver(X, Y, Z, u, v, w, length=0.1, normalize=True)

plt.show()
