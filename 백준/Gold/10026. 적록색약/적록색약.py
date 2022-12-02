from collections import deque

N = int(input())

lst = [input() for _ in range(N)]
used = [[0] * N for _ in range(N)]

r = 0
g = 0
b = 0
rg = 0

def bfs(y, x, color):
    q = deque()
    q.append((y, x))

    while q:
        nowy, nowx = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] in color:
                q.append((ny, nx))
                used[ny][nx] = 1

for i in range(N):
    for j in range(N):
        if not used[i][j]:
            if lst[i][j] == 'R':
                r += 1
                bfs(i, j, 'R')
            elif lst[i][j] == 'G':
                g += 1
                bfs(i, j, 'G')
            elif lst[i][j] == 'B':
                b += 1
                bfs(i, j, 'B')

used = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not used[i][j]:
            if lst[i][j] in ('R', 'G'):
                rg += 1
                bfs(i, j, ('R', 'G'))

print(r + g + b, rg + b)