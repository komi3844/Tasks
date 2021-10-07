p = int(input())
x, y = int(input()), int(input())
r_v_k = (x*p*0.01) + x
k = (y*p*0.01) + y
s = r_v_k + 0.01 * k
print(int(s), int(s * 100 % 100))
