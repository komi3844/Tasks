x = int(input())
y = int(input())
z = int(input())
c = int(input())
if x - z <= 1 and y - c <= 1 and x - z >= -1 and y - c >= -1:
        print('YES')
else:
    print('NO')
