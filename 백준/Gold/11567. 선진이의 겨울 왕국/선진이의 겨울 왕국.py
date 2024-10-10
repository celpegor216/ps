N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

transform = lambda x: int(x) - 1

sy, sx = map(transform, input().split())
ey, ex = map(transform, input().split())


def find(sy, sx, ey, ex):
    q = [(sy, sx)]
    used = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'X':
                used[i][j] = 1

    while q:
        nq = []

        for y, x in q:
            if y == ey and x == ex and used[y][x] > 1:
                return 'YES'

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N and 0 <= nx < M):
                    continue

                if not (ny == ey and nx == ex) and used[ny][nx]:
                    continue

                used[ny][nx] += 1
                nq.append((ny, nx))

        q = nq

    return 'NO'


print(find(sy, sx, ey, ex))