N, M = map(int, input().split())
sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())
lst = [input() for _ in range(N)]


def find():
    used = [[21e8] * M for _ in range(N)]
    used[sy][sx] = 0

    q = [(sy, sx)]
    while q:
        nq = []

        for y, x in q:
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if not(0 <= ny < N and 0 <= nx < M):
                    continue

                if lst[ny][nx] != '0':
                    if used[ny][nx] <= used[y][x] + 1:
                        continue
                    used[ny][nx] = used[y][x] + 1
                else:
                    if used[ny][nx] <= used[y][x]:
                        continue
                    used[ny][nx] = used[y][x]

                nq.append((ny, nx))

        q = nq

    return used[ey][ex]


print(find())