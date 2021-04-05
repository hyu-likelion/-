#3
num = int(input())
num_list = list(map(int, input().split()))
min_val = max_val = num_list[0]
for i in num_list:
    if min_val>i:
        min_val = i
    if max_val<i:
        max_val = i
print(min_val, max_val)
