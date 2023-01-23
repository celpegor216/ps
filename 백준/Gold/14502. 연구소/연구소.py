from copy import deepcopy
from collections import deque

N, M = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []

for n in range(N):
    for m in range(M):
        if lst[n][m] == 0:
            empty.append((n, m))
        elif lst[n][m] == 2:
            virus.append((n, m))

length = len(empty)
used = [0] * length

def dfs(level, now):
    if level == 3:
        bfs()
        return

    for i in range(now + 1, length):
        used[i] = 1
        lst[empty[i][0]][empty[i][1]] = 1
        dfs(level + 1, i)
        used[i] = 0
        lst[empty[i][0]][empty[i][1]] = 0

result = 0

def bfs():
    global result

    q = deque(virus)
    visited = deepcopy(lst)

    while q:
        nowy, nowx = q.popleft()

        visited[nowy][nowx] = 2

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                q.append((ny, nx))

    cnt = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m] == 0:
                cnt += 1

    if cnt > result:
        result = cnt

dfs(0, -1)

print(result)