N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

q = []
for i in range(N):
    for j in range(M):
        if lst[i][j] > 0:
            q.append((i, j))

while q:
    nq = dict()

    for y, x in q:
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx]:
                nq[(ny, nx)] = nq.get((ny, nx), [0, 0])
                nq[(ny, nx)][lst[y][x] - 1] = lst[y][x]

    q = []
    for (y, x), tmp in nq.items():
        value = sum(tmp)
        lst[y][x] = value
        if value != 3:
            q.append((y, x))

results = [0] * 3
for i in range(N):
    for j in range(M):
        if lst[i][j] > 0:
            results[lst[i][j] - 1] += 1

print(*results)