x = int(input())
if 10 < x < 20:
    print(x, 'korov')
elif x % 10 == 1:
    print(x, 'korova')
elif x % 10 in (2, 3, 4):
    print(x, 'korovy')
else:
    print(x, 'korov')
