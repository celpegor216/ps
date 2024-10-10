N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

ry = rx = by = bx = -1
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if lst[i][j] == 'R':
            ry, rx = i, j
            lst[i][j] = '.'
        elif lst[i][j] == 'B':
            by, bx = i, j
            lst[i][j] = '.'


def move(y, x, dy, dx):
    ny, nx = y + dy, x + dx

    while lst[ny][nx] == '.':
        ny += dy
        nx += dx

    if lst[ny][nx] == '#':
        ny -= dy
        nx -= dx

    return ny, nx


def find(ry, rx, by, bx):
    used = set()
    used.add((ry, rx, by, bx))

    q = [(ry, rx, by, bx)]

    time = 0
    while q and time <= 10:
        nq = []

        for ry, rx, by, bx in q:
            if lst[ry][rx] == 'O':
                return 1

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nry, nrx = move(ry, rx, dy, dx)
                nby, nbx = move(by, bx, dy, dx)

                if lst[nby][nbx] == 'O':
                    continue

                if nry == nby and nrx == nbx:
                    if (rx == bx and ry * dy > by * dy) or (ry == by and rx * dx > bx * dx):
                        nby -= dy
                        nbx -= dx
                    else:
                        nry -= dy
                        nrx -= dx

                if (nry, nrx, nby, nbx) not in used:
                    used.add((nry, nrx, nby, nbx))
                    nq.append((nry, nrx, nby, nbx))

        q = nq
        time += 1

    return 0

print(find(ry, rx, by, bx))