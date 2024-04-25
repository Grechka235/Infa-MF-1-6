 import numpy as np

A = [[1, 2, 3],
     [1, 2, 1],
     [3, 2, 0]]

B = [[4, 1, 2],
     [0, 4, 3],
     [1, 1, 1]]


p = [[0.1],
     [1.7],
     [-1.5]]

q = [[-1.6],
     [0.8],
     [1.1]]

r = [[-0.7],
     [1.3],
     [0.2]]

x = np.dot(A,B) # A*B
y = np.dot(x, p) #AB*p
z = np.subtract(y,r) # ABp - r
z = np.squeeze(z)
s = np.dot(z,q) #(ABp-r)*q
print(s)
