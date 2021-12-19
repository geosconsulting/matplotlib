import matplotlib.pyplot as plt

# x = [4, 5, 3, 1, 6, 7]
import numpy as np

x = np.arange(7)

# plt.plot(x, -x**2)
# plt.plot(x, -x**3)
# plt.plot(x, -2*x)
# plt.plot(x, -2**x)

# plt.plot(x, -x**2, 'g', label='-x**2')
# plt.plot(x, -x**3, 'm', label='-x**3')
# plt.plot(x, -2*x, 'r', label='-2*x')
# plt.plot(x, -2**x, 'k', label='-2**x')
# plt.legend()

print(plt.axis())

# plt.plot(x, -x**2, '--', x, -x**3, '-', x, -2*x, '-.', x, -2**x, ':')
plt.plot(x, -x**2, 'g--', x, -x**3, 'r-', x, -2*x, 'b-.', x, -2**x, 'm:')
# plt.plot(x, -x**2, 'g', x, -x**3, 'b', x, -2*x, 'm', x, -2**x, 'r')
plt.legend(['-x**2', '-x**3', '-2*x', '-2**x'], loc='lower center')

plt.title('Simple Plot')
plt.grid(True)
plt.xlabel('x= np.arange(7)')
plt.ylabel('y = f(x)')
plt.xlim(2, 5)
plt.savefig('test.png')
plt.show()

y = x + 12
plt.plot(x, y, color='g', linestyle='--', linewidth=1.5,
         marker='^', markerfacecolor='b', markeredgecolor='k',
         markeredgewidth=1.5, markersize=5)
plt.xticks(range(len(x)), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
plt.grid(True)
plt.show()


# Multiple Plot
plt.subplots_adjust(wspace=0.3, hspace=0.3)

plt.subplot(2, 2, 1)
plt.plot(x, -x**2, 'r')
plt.subplot(2, 2, 2)
plt.plot(x, -x**3)
plt.subplot(2, 2, 3)
plt.plot(x, -2*x)
plt.subplot(2, 2, 4)
plt.plot(x, -2**x)
plt.show()
