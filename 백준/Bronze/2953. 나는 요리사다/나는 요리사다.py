N = 5

result_idx = -1
result_v = -1

for n in range(N):
    total = sum(map(int, input().split()))

    if result_v < total:
        result_v = total
        result_idx = n + 1

print(result_idx, result_v)