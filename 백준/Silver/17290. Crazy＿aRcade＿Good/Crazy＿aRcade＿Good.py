from collections import deque

y, x = map(int, input().split())
N = 10
lst = [input() for _ in range(N)]
bombs = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if lst[i][j] == 'o':
            for k in range(N):
                bombs[i][k] = 1
                bombs[k][j] = 1

q = deque()
used = [[0] * N for _ in range(N)]

q.append((y - 1, x - 1, 0))
used[y - 1][x - 1] = 1

result = 21e8

while q:
    nowy, nowx, nowc = q.popleft()

    if not bombs[nowy][nowx]:
        result = nowc
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
            q.append((ny, nx, nowc + 1))
            used[ny][nx] = 1

print(result)