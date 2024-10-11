N = int(input())

lst = [[-1] * N * 2 + [-1] for _ in range(N)] + [[-1] * (N * 2 + 1)]
tiles = [[0] * (N * 2 + 1) for _ in range(N * 2 + 1)]

tile_idx = 1
for n in range(N):
    idx = 1 if n % 2 else 0

    for _ in range(N - idx):
        a, b = map(int, input().split())
        lst[n][idx] = a
        lst[n][idx + 1] = b
        tiles[n][idx] = tile_idx
        tiles[n][idx + 1] = tile_idx
        idx += 2
        tile_idx += 1

used = [[0] * (N * 2 + 1) for _ in range(N * 2 + 1)]
q = [(0, 0, 0, 1, [1])]
used[0][0] = 1
used[0][1] = 1


result_idx = 1
result_cnt = 1
result_path = [1]

while q:
    nq = []

    for ly, lx, ry, rx, path in q:
        tile_idx = tiles[ly][lx]
        if result_idx < tile_idx:
            result_idx = tile_idx
            result_cnt = len(path)
            result_path = path[:]
        elif result_idx == tile_idx and result_cnt > len(path):
            result_cnt = len(path)
            result_path = path[:]

        # 왼쪽 기준
        for dy, dx in ((-1, 0), (0, -1), (1, 0)):
            ny, nx = ly + dy, lx + dx
            if used[ny][nx] or lst[ny][nx] != lst[ly][lx]:
                continue

            used[ny][nx] = 1
            used[ny][nx - 1] = 1
            nq.append((ny, nx - 1, ny, nx, path + [tiles[ny][nx]]))

        # 오른쪽 기준
        for dy, dx in ((-1, 0), (0, 1), (1, 0)):
            ny, nx = ry + dy, rx + dx
            if used[ny][nx] or lst[ny][nx] != lst[ry][rx]:
                continue

            used[ny][nx] = 1
            used[ny][nx + 1] = 1
            nq.append((ny, nx, ny, nx + 1, path + [tiles[ny][nx]]))

    q = nq


print(result_cnt)
print(*result_path)