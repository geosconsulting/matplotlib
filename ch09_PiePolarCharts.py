import matplotlib.pyplot as plt
import numpy as np

data = np.array([35 , 25 , 25 , 15])

mylabels = ['A' , 'B' , 'C' , 'D']
explode = [0.0 , 0.05 , 0.1 , 0.15]

plt.pie(data , labels=mylabels , explode=explode , shadow=True)
plt.legend(title='Data :')

plt.show()

N = 20
theta = np.linspace(0.0, 2 * np.pi, N)
r = 10 * np.random.rand(N)
size = r * 100

plt.subplot(projection='polar')

# plt.bar(theta, r, bottom=0.0, color=['r', 'g', 'b'], alpha=0.2)
plt.scatter(theta, r, c=theta, s=size, cmap='hsv', alpha=0.5)

plt.show()

