N, M = map(int, input().split())
lst = [list(map(lambda x: 0 if x == '.' else 1, input())) for _ in range(N)]

directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

used = [[0] * M for _ in range(N)]

result = 0
for n in range(N):
    for m in range(M):
        if not lst[n][m]:
            continue

        for dy, dx in directions:
            ny, nx = n + dy, m + dx

            if 0 <= ny < N and 0 <= nx < M:
                if lst[ny][nx] == 1:
                    result += 1
                else:
                    used[ny][nx] += 1

result //= 2

maxv = 0
for i in range(N):
    for j in range(M):
        if not lst[i][j]:
            maxv = max(maxv, used[i][j])

print(result + maxv)