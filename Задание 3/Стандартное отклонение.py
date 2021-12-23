a = int(input())
E, D1, i = a, 0, 1
while a != 0:
    E = ((i - 1) * E + a) / i   # новое среднее значение через предыдущее
    D1 += a**2
    i += 1
    a = int(input())
print(((D1 - (i - 1) * E**2) / (i - 2))**0.5)
