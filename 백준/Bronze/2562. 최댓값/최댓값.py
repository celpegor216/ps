N = 9
lst = [int(input()) for _ in range(N)]

result_idx = -1
result_v = -1

for i in range(N):
    if result_v < lst[i]:
        result_v = lst[i]
        result_idx = i

print(result_v)
print(result_idx + 1)