time = int(input())
h = (time // (60*60)) % 24
m = (time // 60) % 60
s = time % 60
print(h, ':', m // 10, m % 10, ':', s // 10, s % 10, sep='')
