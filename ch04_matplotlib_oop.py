import matplotlib.pyplot as plt
import numpy as np

x = np.arange(7)

# Single Plot
# fig, ax = plt.subplots()
# ax.plot(x, -x**2, label='-x**2')
# ax.plot(x, -x**3, label='-x**3')
# ax.plot(x, -2*x, label='-2*x')
# ax.plot(x, -2**x, label='-2**x')
# ax.set_xlabel('x = np.arange(7)')
# ax.set_ylabel('y = f(x)')
# ax.set_title('Simple Plot Demo')
# ax.legend()
# ax.grid(True)
# ax.text(0, -25, "Simple Plot Demo")
# plt.show()


# Single Plot
fig, axs = plt.subplots(2, 2)
plt.subplots_adjust(wspace=0.3,hspace=0.3)
axs[0, 0].plot(x, -x**2)
axs[0, 1].plot(x, -x**3, 'r')
axs[1, 0].plot(x, -2*x)
axs[1, 1].plot(x, -2**x, 'm')
plt.show()