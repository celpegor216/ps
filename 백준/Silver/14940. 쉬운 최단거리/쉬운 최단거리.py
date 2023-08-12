from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]

sy, sx = -1, -1
for n in range(N):
    if sy != -1:
        break

    for m in range(M):
        if lst[n][m] == 2:
            sy = n
            sx = m
            break

q = deque()
q.append((sy, sx, 0))

while q:
    nowy, nowx, nowc = q.popleft()

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < M and not result[ny][nx] and lst[ny][nx] == 1:
            result[ny][nx] = nowc + 1
            q.append((ny, nx, nowc + 1))

for n in range(N):
    for m in range(M):
        if lst[n][m] == 1 and not result[n][m]:
            result[n][m] = -1

for line in result:
    print(*line)