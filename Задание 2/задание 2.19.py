A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
A1, B1, C1 = sorted((A1, B1, C1))
A2, B2, C2 = sorted((A2, B2, C2))
if A1 == A2 and B1 == B2 and C1 == C2:
    print('Boxes are equal')
elif A1 <= A2 and B1 <= B2 and C1 <= C2:
    print('The first box is smaller than the second one')
elif A1 >= A2 and B1 >= B2 and C1 >= C2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
