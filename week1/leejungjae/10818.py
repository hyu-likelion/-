import sys 

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

Max = -1000000
Min = 1000000

for num in arr:
  Max = max(Max,num)
  Min = min(Min,num)

print(Min,Max)
