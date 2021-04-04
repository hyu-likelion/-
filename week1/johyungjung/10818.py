_ = int(input())
arr = list(map(int, input().split()))

ret_min = ret_max = arr[0]
for val in arr:
  if val > ret_max:
    ret_max = val
  if val < ret_min:
    ret_min = val
print(ret_min, ret_max)
