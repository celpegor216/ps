N, M = map(int, input().split())

lst = [[0] * (M + 2)] + [[0] + list(map(lambda x: 0 if x == '0' else -1, input().split())) + [0] for _ in range(N)] + [[0] * (M + 2)]

directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
directions_changed = (1, 0, 3, 2)

idx = 1
starts = []
for i in range(1, N + 1):
    lst[i][0] = idx
    starts.append((i, 0, 0, idx))
    idx += 1
for j in range(1, M + 1):
    lst[N + 1][j] = idx
    starts.append((N + 1, j, 1, idx))
    idx += 1
for i in range(N, 0, -1):
    lst[i][M + 1] = idx
    idx += 1
for j in range(M, 0, -1):
    lst[0][j] = idx
    idx += 1



result = [0] * idx

for sy, sx, sd, sn in starts:
    dy, dx = directions[sd]
    ny, nx = sy + dy, sx + dx
    nd = sd

    while lst[ny][nx] <= 0:
        if lst[ny][nx] == -1:
            nd = directions_changed[nd]

        dy, dx = directions[nd]
        ny += dy
        nx += dx

    en = lst[ny][nx]
    result[sn] = en
    result[en] = sn

print(*result[1:])