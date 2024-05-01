N, M = map(int, input().split())
lst = list(map(int, input().split()))

now = [x for x in range(1, N + 1)]

result = 0
for m in range(M):
    idx = now.index(lst[m])

    result += min(idx, N - m - idx)
    now = now[idx + 1:] + now[:idx]

print(result)