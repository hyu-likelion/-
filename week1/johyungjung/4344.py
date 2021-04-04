test_cases = int(input())
for _ in range(test_cases):
  arr = list(map(int, input().split()))
  avg = sum(arr[1:])/arr[0]
  print("{:0.3f}%".format(len([i for i in arr[1:] if i > avg])/arr[0]*100))
