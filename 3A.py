x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
z = int(input('Введите значение z: '))

if (x*y*z) > (2 * x**2 + 3*y):
    maxx = x*y*z
else:
    maxx = (2 * x**2 + 3*y)

if z < x:
    minn = z
else:
    minn = x

u = maxx/minn
print(u)
