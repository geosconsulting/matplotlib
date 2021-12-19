import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

data = np.random.randn(10)

# for active_style in plt.style.available:
#
#     plt.title(active_style)
#     plt.style.use(active_style)
#     plt.plot(data)
#     plt.show()

plt.style.use('default')

# fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True)
# plt.show()

# fig = plt.figure(constrained_layout=True)
# specs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)
# ax1 = fig.add_subplot(specs[0, 0])
# ax2 = fig.add_subplot(specs[0, 1])
# ax3 = fig.add_subplot(specs[1, 0])
# ax4 = fig.add_subplot(specs[1, 1])
# plt.show()

fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3, 3)
ax1 = fig.add_subplot(gs[0, :])
ax1.set_title('gs[0, :]')
ax2 = fig.add_subplot(gs[1, :])
ax2.set_title('gs[1, :]')
ax3 = fig.add_subplot(gs[2, :])
ax3.set_title('gs[2, :]')
plt.show()

