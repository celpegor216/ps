# 쓰레기 옆을 지나가는 칸의 개수 != 몇 개의 쓰레기 옆을 지나가는가?
# 문제를 제대로 읽자...

from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

MAXV = 21e8
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
near = [[0] * M for _ in range(N)]
q = deque()
used = [[[MAXV, MAXV] for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'S':
            used[i][j] = [0, 0]
            q.append((i, j, 0, 0))
        elif lst[i][j] == 'g':
            for dy, dx in directions:
                ny, nx = i + dy, j + dx
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '.':
                    near[ny][nx] = 1

result = [MAXV, MAXV]
while q:
    y, x, g, n = q.popleft()

    if used[y][x][0] < g or (used[y][x][0] == g and used[y][x][1] < n) or result[0] < g or (result[0] == g and result[1] < n):
        continue

    if lst[y][x] == 'F':
        if result[0] > g:
            result = [g, n]
        elif result[0] == g:
            result[1] = min(result[1], n)
        continue

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            ng, nn = g, n

            if lst[ny][nx] == 'g':
                ng += 1
            elif lst[ny][nx] == '.' and near[ny][nx]:
                nn += 1
            
            if used[ny][nx][0] > ng or (used[ny][nx][0] == ng and used[ny][nx][1] > nn):
                used[ny][nx] = [ng, nn]
                q.append((ny, nx, ng, nn))

print(*result)