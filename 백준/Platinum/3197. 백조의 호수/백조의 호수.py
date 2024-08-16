from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

MAX = int(21e8)
used_ice = [[MAX] * M for _ in range(N)]
used_swan = [[MAX] * M for _ in range(N)]

q_swan = deque()
ey = ex = -1
q_ice = deque()

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'L':
            used_ice[i][j] = 0
            if q_swan:
                ey = i
                ex = j
            else:
                q_swan.append((i, j, 0))
                used_swan[i][j] = 0
        elif lst[i][j] == '.':
            used_ice[i][j] = 0
        else:
            flag = 0
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 'X':
                    flag = 1
                    break
            if flag:
                q_ice.append((i, j, 1))
                used_ice[i][j] = 1

# 얼음을 전부 녹임
while q_ice:
    y, x, c = q_ice.popleft()

    if used_ice[y][x] < c:
        continue

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and used_ice[ny][nx] > c + 1:
            used_ice[ny][nx] = c + 1
            q_ice.append((ny, nx, c + 1))

result = MAX
while q_swan:
    y, x, c = q_swan.popleft()

    if used_swan[y][x] < c:
        continue

    if y == ey and x == ex:
        result = min(result, c)
        continue

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            nc = max(c, used_ice[ny][nx])
            if used_swan[ny][nx] > nc:
                used_swan[ny][nx] = nc
                q_swan.append((ny, nx, nc))

print(result)