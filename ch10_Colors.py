import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(5 , 6)

# plt.pcolor(data, cmap='YlGnBu_r')

N = 100
X , Y = np.meshgrid(np.linspace(-5 , 5 , N) , np.linspace(-4 , 4 , N))
Z = (X ** 2 + Y ** 2)

# plt.pcolor(X, Y, Z, cmap='YlGnBu_r', shading='auto')
# plt.pcolor(X, Y, Z, cmap='YlGnBu_r', shading='nearest')

# plt.pcolormesh(X , Y , Z ,
#                cmap='YlGnBu_r' ,
#                shading='auto')

nrows = ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
z = np.arange(nrows * ncols).reshape(nrows , ncols)
plt.pcolormesh(x , y , z ,
               # shading='flat' ,
               shading='auto' ,
               cmap='coolwarm')

# img = plt.imshow(Z, cmap='YlGnBu_r')
plt.colorbar()

plt.show()
