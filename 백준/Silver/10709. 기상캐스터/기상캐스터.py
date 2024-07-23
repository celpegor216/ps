N, M = map(int, input().split())
lst = [input() for _ in range(N)]

used = [[-1] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if lst[n][m] == 'c':
            used[n][m] = 0

            j = m + 1
            while j < M:
                used[n][j] = used[n][j - 1] + 1
                j += 1

for line in used:
    print(*line)