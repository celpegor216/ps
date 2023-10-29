from collections import deque
from copy import deepcopy

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lands = []
used = [[0] * N for _ in range(N)]

cnt = -1

for i in range(N):
    for j in range(N):
        if not used[i][j] and lst[i][j]:
            used[i][j] = cnt

            q = deque()
            q.append((i, j))

            land = []

            while q:
                nowy, nowx = q.popleft()

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = nowy + dy, nowx + dx

                    if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
                        if lst[ny][nx]:
                            used[ny][nx] = cnt
                            q.append((ny, nx))
                        elif (ny, nx) not in land:
                            land.append((ny, nx))

            lands.append(land)

            cnt -= 1

cnt = -1
result = 21e8

for land in lands:
    q = deque()
    tmp = deepcopy(used)

    for y, x in land:
        tmp[y][x] = 1
        q.append((y, x, 1))

    while q:
        nowy, nowx, nowc = q.popleft()

        if nowc >= result:
            continue

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx

            if 0 <= ny < N and 0 <= nx < N:
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = nowc + 1
                    q.append((ny, nx, nowc + 1))
                elif tmp[ny][nx] < 0 and tmp[ny][nx] != cnt:
                    result = min(result, nowc)

    cnt -= 1

print(result)