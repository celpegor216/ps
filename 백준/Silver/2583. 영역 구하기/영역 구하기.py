from collections import deque

M, N, K = map(int, input().split())
lst = [[0] * M for _ in range(N)]

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            lst[x][y] = 1

used = [[0] * M for _ in range(N)]

results = []

for n in range(N):
    for m in range(M):
        if not lst[n][m] and not used[n][m]:
            q = deque()
            q.append((n, m))

            used[n][m] = 1

            cnt = 0

            while q:
                x, y = q.popleft()

                cnt += 1

                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and not lst[nx][ny] and not used[nx][ny]:
                        q.append((nx, ny))
                        used[nx][ny] = 1
            
            results.append(cnt)

print(len(results))
print(*sorted(results))