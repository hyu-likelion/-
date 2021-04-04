a, b = map(lambda x: int("".join(list(reversed(x)))), input().split())
print(a if a>b else b)
