a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print('acute')
    else:
        if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
            print('obtuse')
        else:
            print('rectangular')
else:
    print('impossible')
