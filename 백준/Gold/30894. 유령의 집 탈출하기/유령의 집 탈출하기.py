N, M = map(int, input().split())

sy, sx, ey, ex = map(lambda x: int(x) - 1, input().split())

# 빈칸(.): 석준이가 움직일 수 있는 공간을 의미합니다.
# 벽(#): 석준이가 움직일 수 없는 공간을 의미합니다.
# 유령(0, 1, 2, 3): 각 숫자는 유령이 바라보는 초기 방향을 의미합니다. (0 : 오른쪽, 1 : 아래, 2 : 왼쪽, 3 : 위)
lst = []
ghosts = []
for i in range(N):
    tmp = input()
    for j in range(M):
        if tmp[j] not in '.#':
            ghosts.append([i, j, int(tmp[j])])
    lst.append(tmp)

directions = ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0))

ghost_useds = []

# 각 유령은 매초 시계 방향으로  90°씩 회전하며, 회전하는 동안에는 석준이를 볼 수 없습니다.
for _ in range(4):
    used = [[0] * M for _ in range(N)]

    for ghost in ghosts:
        y, x, d = ghost
        used[y][x] = 1
        dy, dx = directions[d]
        y += dy
        x += dx

        # 어떤 유령이 바라보는 방향에 벽이나 다른 유령이 존재하는 경우,
        # 시야가 가로막혀 그 뒤의 공간은 볼 수 없습니다.
        while 0 <= y < N and 0 <= x < M and lst[y][x] == '.':
            used[y][x] = 1
            y += dy
            x += dx
        ghost[-1] = (ghost[-1] + 1) % 4

    ghost_useds.append(used)


def find(sy, sx, ey, ex):
    q = [(sy, sx, 0)]

    # time % 4 시점에 방문한 적이 있는가?
    used = [[[0] * 4 for _ in range(M)] for _ in range(N)]
    used[sy][sx][0] = 1

    while q:
        nq = []

        for y, x, t in q:
            # 유령의 집을 탈출하는 데 걸리는 최소 시간을 출력합니다.
            if y == ey and x == ex:
                return t

            # 석준이는 매초 상하좌우로 인접한 빈칸으로 이동하거나 제자리에 머무를 수 있습니다.
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                nt = t + 1

                if 0 <= ny < N and 0 <= nx < M and not used[ny][nx][nt % 4] and not ghost_useds[nt % 4][ny][nx] and lst[ny][nx] == '.':
                    used[ny][nx][nt % 4] = 1
                    nq.append((ny, nx, nt))

        q = nq


    # 만약 유령에게 발견되지 않고 탈출할 방법이 없다면, GG를 출력합니다.
    return 'GG'


print(find(sy, sx, ey, ex))