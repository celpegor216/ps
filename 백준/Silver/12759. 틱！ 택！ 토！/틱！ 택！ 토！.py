N = 3
side = int(input()) - 1
rows = [[0] * 2 for _ in range(N)]
cols = [[0] * 2 for _ in range(N)]
cross = [[0] * 2 for _ in range(2)]    # 좌상우하, 좌하우상

for _ in range(N * N):
    y, x = map(lambda x: int(x) - 1, input().split())
    rows[y][side] += 1
    cols[x][side] += 1
    if y == x:
        cross[0][side] += 1
    if y + x == 2:
        cross[1][side] += 1

    if rows[y][side] == 3 or cols[x][side] == 3 or cross[0][side] == 3 or cross[1][side] == 3:
        print(side + 1)
        break

    side = 0 if side else 1
else:
    print(0)