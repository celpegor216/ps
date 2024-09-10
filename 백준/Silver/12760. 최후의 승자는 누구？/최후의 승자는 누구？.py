N, M = map(int, input().split())
lst = [sorted(map(int, input().split())) for _ in range(N)]

result = [0] * N
for j in range(M):
    maxv = 0
    max_idx = []
    for i in range(N):
        if lst[i][j] > maxv:
            maxv = lst[i][j]
            max_idx = [i]
        elif lst[i][j] == maxv:
            max_idx.append(i)

    for idx in max_idx:
        result[idx] += 1

maxv = max(result)
for i in range(N):
    if result[i] == maxv:
        print(i + 1, end=' ')