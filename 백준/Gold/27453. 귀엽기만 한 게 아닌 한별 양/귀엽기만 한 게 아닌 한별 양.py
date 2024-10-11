N, M, K = map(int, input().split())

lst = [list(input()) for _ in range(N)]

sy = sx = ey = ex = -1

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'S':
            sy, sx = i, j
            lst[i][j] = 0
        elif lst[i][j] == 'H':
            ey, ex = i, j
            lst[i][j] = 0
        elif lst[i][j] == 'X':
            lst[i][j] = -1
        else:
            lst[i][j] = int(lst[i][j])


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def find(sy, sx, ey, ex):
    q = [(sy, sx, -1, -1, [0, 0, 0])]

    # used[i][j][d]: i, j에 d방향으로 온 적 있는가?
    used = [[[0] * 4 for _ in range(M)] for _ in range(N)]

    time = 0
    while q:
        nq = []

        for y, x, by, bx, path in q:
            if y == ey and x == ex:
                return time

            for d in range(4):
                dy, dx = directions[d]
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N and 0 <= nx < M) or used[ny][nx][d] or lst[ny][nx] == -1 or (ny == by and nx == bx):
                    continue

                if path[1] + path[2] + lst[ny][nx] > K:
                    continue

                used[ny][nx][d] = 1
                nq.append((ny, nx, y, x, [path[1], path[2], lst[ny][nx]]))

        q = nq
        time += 1

    # 만약 안전하게 귀가하지 못한다면 -1을 출력
    return -1

print(find(sy, sx, ey, ex))