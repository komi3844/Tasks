A, B, C = int(input()), int(input()), int(input())
E, D = int(input()), int(input())
if (A <= E and B <= D) or (A <= D and B <= E):
    print('YES')
elif (A <= E and C <= D) or (A <= D and C <= E):
    print('YES')
elif (C <= E and B <= D) or (C <= D and B <= E):
    print('YES')
else:
    print('NO')
