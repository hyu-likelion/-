a = int(input())
d = list(map(int, input().split()))

min_num = d[0]
max_num = d[0]
for i in d:
    if min_num>i:
        min_num = i
    if max_num<i:
        max_num = i
print(min_num, max_num)