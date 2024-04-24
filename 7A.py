import numpy as np 
A = np.array([[1, 2, 3], [1, 2, 1], [3, 2, 0]])
B = np.array([[4, 1, 2], [0, 4, 3], [1, 1, 1]])
r = np.array([[-0.7], [1.3], [0.2]])
q = np.array([[-1.6], [0.8], [1.1]])
p = np.array([[0.1], [1.7], [-1.5]])

x = sum((A[i] * B[i] * p[i] - r[i] * q[i] for i in range(3)))

print("Скалярное произведение векторов:", x)
