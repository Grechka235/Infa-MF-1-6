 N = int(input("Введите N: "))

X=[0.1,0.3, 0.4, 0.7, 1]

print('                 ТАБЛИЦА                ')
print('                ---------               ')
print('           (X)               (S)        ')

for x in X:
    s = 0
    for k in range(1,N+1):
            u = ((-1)**(k+1)) * ((x**k)/(k + 1)**2)
            s += u
    print("        X= %.3f          S= %.3f           " % (x,s))
print ('                .   .   .                     ')
