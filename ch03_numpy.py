import numpy as np

l1 = [1, 2, 3]
x = np.array(l1, dtype=np.int16)

print(x[1])


for i in range(len(l1)):
    print(x[i])

for i in enumerate(x):
    print(i[0], i[1])

print(x[-1])


x1 = np.array([[1, 2, 3], [4, 5, 6]], np.int16)

print(x1[1, 2])

print(x1[:, 0])
print(x1[:, 1])

x2 = np.array([[[1, 2, 3], [4, 5, 6]], [[0, -1, -2], [-3, -4, -5]]], np.int16)

print(x2[0, 0, 0])

print(x2[0])
print(x2[1])

# Second arra second row second column
print(x2[1, 1, 1])

x3 = np.array([[[1, 2, 3, 5], [4, 5, 6, 6]],
               [[0, -1, -2, 12], [-3, -4, -5, 1]],
               [[10, -11, -12, 5], [-23, -24, -25, 6]]], np.int16)

print(x3[1][0][1:-1])

print(x3.ndim)
pi_greek = np.pi

x = np.empty([3, 3], np.uint8)

y = np.eye(5, dtype=np.uint8)

x = np.identity(5, dtype= np.uint8)

x = np.ones((2, 5, 5), dtype=np.int16)

x_all5 = np.full((3, 3, 3), dtype=np.int16, fill_value = 5)

x = np.tri(3, 3, k=0, dtype=np.uint16)