N, M = 10, 9
sy, sx = map(int, input().split())
ey, ex = map(int, input().split())


moves = (
    [(-1, 0), (-2, 1), (-3, 2)],
    [(-1, 0), (-2, -1), (-3, -2)],
    [(0, 1), (-1, 2), (-2, 3)],
    [(0, 1), (1, 2), (2, 3)],
    [(1, 0), (2, 1), (3, 2)],
    [(1, 0), (2, -1), (3, -2)],
    [(0, -1), (1, -2), (2, -3)],
    [(0, -1), (-1, -2), (-2, -3)]
)


def find():
    q = [(sy, sx)]

    used = [[0] * M for _ in range(N)]
    used[sy][sx] = 1

    result = 0
    while q:
        nq = []

        for y, x in q:
            if y == ey and x == ex:
                return result

            for move in moves:
                for d in range(3):
                    dy, dx = move[d]
                    ny, nx = y + dy, x + dx
                    if not(0 <= ny < N and 0 <= nx < M) or d < 2 and ny == ey and nx == ex:
                        break
                else:
                    nq.append((ny, nx))
                    used[ny][nx] = 1

        q = nq
        result += 1

    return -1


print(find())