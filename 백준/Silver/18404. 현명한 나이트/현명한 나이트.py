from collections import deque

N, M = map(int, input().split())
y, x = map(int, input().split())
others = [list(map(int, input().split())) for _ in range(M)]

used = [[0] * (N + 1) for _ in range(N + 1)]
used[y][x] = 1

q = deque()
q.append((y, x, 0))

while q:
    nowy, nowx, nowc = q.popleft()

    for dy, dx in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
        ny, nx = nowy + dy, nowx + dx
        if 1 <= ny <= N and 1 <= nx <= N and not used[ny][nx]:
            used[ny][nx] = nowc + 1
            q.append((ny, nx, nowc + 1))

for ny, nx in others:
    print(used[ny][nx], end=' ')