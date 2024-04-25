№1

x = 2
y = 2
z = 2

result = x**(y*z) + z**(x*y) + y**(z**x)
print(result)

№2

import math

a = 2
b = 1
x = 1

result = math.exp(a - b) + (math.sin(x + 2) - 4.3)**2
print(result)

№3

import math

x = 2

result = (math.sin(x) + 2) / (math.tan(x**2) + abs(x - 1))
print(result)

№4

import math

a = 2
b = 2.5
c = 0.3
x = 1

result = (math.asin(b**3 - 3*b**2*a + 3*b*a**2 - a**3) + math.log(x**2)**2) / (3*a*b*c)
print(result)


(Варианты заданий B)

import math

g = 3
h = -3

u = g + 3*h
t = math.cos(2*g + h)**2

result = (math.sqrt(math.sin(4*u))**3 + 8 + 4) / (u + t + 1)
print(result)
