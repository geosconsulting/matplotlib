import numpy as np
import matplotlib.pyplot as plt

x = [1, 3, 5, 1, 2, 4, 4, 2, 5, 4, 3, 1, 2]
# n_bins = 5
# plt.hist(x, bins=n_bins)
# plt.show()

# np.random.seed(31415)
# n_points = 10000
# n_bins = 15
# x = np.random.randn(n_points)
#
# y = np.random.randn(n_points)
# plt.hist2d(x, y, bins=50)


# x = np.arange(-3, 3, 0.005)
# y = np.arange(-3, 3, 0.005)
# X, Y = np.meshgrid(x, y)
# # Z = (X + Y)
# Z = (X**2 + Y**2)
#
# out = plt.contour(X, Y, Z)
# plt.clabel(out, inline=True, fontsize=10)
# plt.colorbar(out)


# Y, X = np.mgrid[-5:5:200j, -5:5:300j]
# U = X**2 + Y**2
# V = X + Y
# plt.streamplot(X, Y, U, V, density=[0.5, 0.75])
# plt.streamplot(X, Y, U, V, color=V, linewidth=1, cmap='cool')
# plt.streamplot(X, Y, U, V, color=V, linewidth=X, cmap='cool')

X = np.arange(-5, 5, 0.5)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
plt.quiver(X, Y, U, V)

plt.show()

