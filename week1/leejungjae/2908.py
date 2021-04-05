import sys 

input = sys.stdin.readline

a,b = map(list,input().split())

a.reverse()
b.reverse()

ar = int("".join(a))
br = int("".join(b))

print(max(ar,br))
