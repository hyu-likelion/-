import sys 

input = sys.stdin.readline

n = int(input())

for i in range(n):
  tmp =  list(map(int,input().split()))
  m, data = tmp[0], tmp[1:]

  # 평균
  average = sum(data)/m

  # 평균 이상
  num = 0

  for j in range(m): 
    if data[j] > average:
      num = num + 1

  print( format(round((num/m)*100,3),".3f")+'%')