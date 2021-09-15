x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8:
    print('NO')
elif (x1 + y1) % 2 != (x2 + y2) % 2:
    print('NO')
elif x2 + y2 < x1 + y1:
    print('NO')
elif x2 - y2 > x1 - y1:
    print('NO')
else:
    print('YES')
