A, B = map(int, input().split())
c = int(str(A)[::-1])
d = int(str(B)[::-1])
if c>d:
    print(c)
else:
    print(d)