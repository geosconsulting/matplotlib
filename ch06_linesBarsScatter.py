import numpy as np
import matplotlib.pyplot as plt

# t = np.arange(0.01, 10, 0.01)

# plt.plot(t)
# plt.semilogx(t, np.cos(2 * np.pi * t))

# x = np.linspace(0, 2*np.pi, 100)
# y = np.sin(x)
# ye = np.random.rand(len(x))/2
# plt.errorbar(x, y, yerr=ye)
# plt.show()

# x = np.arange(4)
# y = np.random.rand(4)
# plt.bar(x, y)

# y = np.random.rand(3 , 4)
# # plt.bar(x + 0.00 , y[0] , color='b' , width=0.25)
# # plt.bar(x + 0.25 , y[1] , color='g' , width=0.25)
# # plt.bar(x + 0.50 , y[2] , color='r' , width=0.25)
# plt.barh(x + 0.00 , y[0] , color='b' , height=0.25)
# plt.barh(x + 0.25 , y[1] , color='g' , height=0.25)
# plt.barh(x + 0.50 , y[2] , color='r' , height=0.25)

N = 1000
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
size = 20
plt.scatter(x, y, s=size, c=colors, alpha=1)
plt.show()
