 import numpy as np
import matplotlib.pyplot as plt

y = lambda x:  2*(x**4) + 8 * (x**3) - 27 * (x**2) - 140 * x + 8;

x = np.linspace(-5, 5,21)
print(' x   y(x)')
for temp in x :
    print ( temp, y(temp))
xmax = max(x,key=y)
print('Xmax = ',xmax,end=' ')
fmax = max(y(x))
print('Ymax = ',fmax)
xmin = min(x,key=y)
print('Xmin = ',xmin,end=' ')
fmin = min(y(x))
print('Ymin = ',fmin)

fig = plt.subplots()

plt.plot(x, y(x))

plt.show()
