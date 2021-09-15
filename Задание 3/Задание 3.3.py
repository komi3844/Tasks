import math

x = float(input())
y1 = int(x)
if x - y1 < 0.5:
    print(y1)
else:
    print(math.ceil(x))
