N, K = map(int, input().split())
lst = [0] + list(map(int, input().split()))
shuffles = [0] + list(map(int, input().split()))

result = [0] * (N + 1)
for k in range(K):
    if not k:
        for n in range(1, N + 1):
            result[shuffles[n]] = lst[n]
    else:
        tmp = result[:]
        for n in range(1, N + 1):
            result[shuffles[n]] = tmp[n]

print(*result[1:])