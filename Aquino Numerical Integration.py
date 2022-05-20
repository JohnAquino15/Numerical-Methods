#John Benedict Aquino
#Numerical Methods Activity
#May 20, 2022

from math import sin


def f(x): return sin(3 * x)


a = 0
b = 0.6
n = 6
h = (b - a) / n
S = h * (f(a) + f(b))
for i in range(1, n):
    S = S + f(a + i * h)
Integral = h * S
print('Integral = %.1f' % Integral)
