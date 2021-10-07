p = float(input())
x = float(input())
y = float(input())
k = int(input())
i = 0
while i != k:
    i += 1
    x = x * (p * 0.01 + 1)
    y = y * (p * 0.01 + 1)
    k3 = y * 0.01 + x + 10 ** -7
    x = int(k3)
    y = int(100 * (k3 - x))
print(x, y)
