import numpy as np
import matplotlib.pyplot as plt


def f(x , y):
    return x ** 3 + y ** 2


# n = 10
# x = np.linspace(-3 , 3 , 8 * n)
# y = np.linspace(-3 , 3 , 6 * n)
#
# X , Y = np.meshgrid(x , y)
#
# Z = f(X , Y)
#
# plt.imshow(Z , interpolation='nearest' , cmap='cool' , origin='lower')
# plt.axis('off')
# plt.show()


# n = 256
# x = np.linspace(-3 , 3 , n)
# y = np.linspace(-3 , 3 , n)
# X , Y = np.meshgrid(x , y)
# plt.contourf(X , Y , f(X , Y) , 8 , alpha=0.75 , cmap='hot')
#
# C = plt.contour(X , Y , f(X , Y) , 8 , colors='black')
# plt.clabel(C , inline=1 , fontsize=10)
#
# plt.axis('off')
# plt.show()


# y = np.random.randn(1000)
# plt.xkcd()
# plt.hist(y)
# plt.show()

y = np.random.randn(1000)
plt.xkcd()
plt.hist(y , bins=30 ,
         range=[-3.5 , 3.5] ,
         facecolor='r' ,
         alpha=0.6 ,
         edgecolor='k')
plt.grid()
plt.show()


