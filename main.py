import numpy as np
from math import factorial

n = int(input('Введите количество каналов  '))
M = int(input('Введите емкость очереди  '))
lmd = 2
counts = 30
UPH = 60 / 30
b = 3 / 2

mu = 1 / b
y = lmd / mu

print(UPH, b, mu, y)
pc = 0
p0r = 0
for i in range(1, n + 1, 1):
    p0f = (y ** i) / factorial(i)
    ptemp = p0f
    p0r = p0r + ptemp

p0 = round((1 + p0r + ((y ** (n + 1)) / (factorial(n) * n)) * (1 - ((y / n) ** M)) / (1 - (y / n))) ** -1, 4)
print(p0)

pi = round(((y ** (n + M)) / ((n ** M) * factorial(n))) * p0, 4)
print(pi)

Q = 1 - pi
lmdderiv = lmd * Q
kmean = lmdderiv / mu

I = round(((y ** (n + 1)) / (n * factorial(n))) *
((((1 - ((y / n) ** M)) * (M + 1 - (M * y) / n)) / (1 - (y / n)) ** 2)) * p0, 1)

print(I)
W=I/lmd
m=i+kmean
u=m/lmd

n_vals = [2,4]
M_vals= [4,6]
results = []
for n in n_vals:
    for M in M_vals:
        pc = 0
        p0r = 0
        for i in range(1, n + 1, 1):
            p0f = (y ** i) / factorial(i)
            ptemp = p0f
            p0r = p0r + ptemp
            p0 = round((1 + p0r + ((y ** (n + 1)) / (factorial(n) * n)) * (1 - ((y / n) ** M)) / (1 - (y / n))) ** -1,
            4)
            pi = round(((y ** (n + M)) / ((n ** M) * factorial(n))) * p0, 4)
            Q = 1 - pi
            lmdderiv = lmd * Q
            kmean = lmdderiv / mu
            I = round(((y ** (n + 1)) / (n * factorial(n))) *
            ((((1 - ((y / n) ** M)) * (M + 1 - (M * y) / n)) / (1 - (y / n)) ** 2)) * p0, 1)
            W = I / lmd
            m = i + kmean
            u = m / lmd


            results.append((n, M, p0, pi, Q, lmdderiv, kmean, I, W, m, u))

results=np.array(results)

print(results)