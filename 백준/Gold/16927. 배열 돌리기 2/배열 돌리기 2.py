N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

K = min(N, M) // 2
for k in range(K):
    # 경로
    path = [(k, k)]
    y = x = k
    d = 0
    while 1:
        dy, dx = directions[d]
        ny, nx = y + dy, x + dx

        if not (k <= ny < N - k and k <= nx < M - k):
            d = (d + 1) % 4
            dy, dx = directions[d]
            ny, nx = y + dy, x + dx

        if ny == nx == k:
            break

        path.append((ny, nx))
        y, x = ny, nx

    # 회전 수
    size = len(path)
    cnt = R % size

    for i in range(size):
        y, x = path[i]
        ny, nx = path[(i + cnt) % size]
        result[ny][nx] = lst[y][x]

for line in result:
    print(*line)