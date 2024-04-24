 import math

t = float(input('Введите t: '))

a = 2*t + 1
b = -1 *(t -3)
c = t + 2

if a == 0:   # t = -0.5
    x = (c * -1) / b
    print(f' x = {round(x,3)}')
    exit()

discr = (b**2) - 4*a*c
print('Дискременант D = ', round(discr,3))

if discr > 0:   # t = -0.1
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b - math.sqrt(discr)) / (2*a)
    print(f'x1 = {round(x1,3)} x2 = {round(x2,3)}')
elif discr == 0:
    x = -b / (2*a)
    print('x = ',x)
else:  # t = 1
    print('Корней нет')
