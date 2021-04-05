import sys 

input = sys.stdin.readline

word = input().rstrip().upper()

count = [ 0 for _ in range(26) ]

for idx in range(len(word)):
  countIdx = ord(word[idx]) -  ord('A') 
  count[countIdx] = count[countIdx] + 1

val = 0
maxvalus = []

for idx in range(26):
  if val < count[idx]:
    maxvalus = [idx]
    val = count[idx]

  elif val == count[idx]:
    maxvalus.append(idx)

if len(maxvalus) > 1 :
  print('?')
else :
  print(chr(maxvalus[0] +  ord('A') ))

