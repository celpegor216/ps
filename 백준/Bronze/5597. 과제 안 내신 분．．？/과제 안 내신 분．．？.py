N = 28
lst = set([int(input()) for _ in range(28)])

result = sorted(set(range(1, 31)) - lst)

print(result[0])
print(result[1])