# dfs 시간 초과


from collections import deque


N, M = map(int, input().split())
lst = [input() for _ in range(N)]

checks = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'S':
            sy, sx = i, j
        elif lst[i][j] == 'C':
            checks.append((i, j))

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
MAX = 21e8
result = MAX


def bfs(sy, sx, ey, ex, sds):
    res = MAX
    resd = []

    for sd in sds:
        q = deque()
        q.append((sy, sx, sd, 0))

        used = [[[0] * 4 for _ in range(M)] for _ in range(N)]

        while q:
            nowy, nowx, nowd, nowt = q.popleft()

            if nowy == ey and nowx == ex:
                if nowt < res:
                    res = nowt
                    resd = [nowd]
                elif nowt == res:
                    resd.append(nowd)
                continue

            for nxtd in range(4):
                if nxtd == nowd:
                    continue

                ny, nx = nowy + directions[nxtd][0], nowx + directions[nxtd][1]

                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != '#' and not used[ny][nx][nxtd]:
                    used[ny][nx][nxtd] = 1
                    q.append((ny, nx, nxtd, nowt + 1))

    return res, set(resd)

# s > c1 > c2
res1, d1 = bfs(sy, sx, *checks[0], [-1])
if d1:
    res2, _ = bfs(*checks[0], *checks[1], d1)
    result = min(result, res1 + res2)
# s > c2 > c1
res1, d1 = bfs(sy, sx, *checks[1], [-1])
if d1:
    res2, _ = bfs(*checks[1], *checks[0], d1)
    result = min(result, res1 + res2)

print(result if result != MAX else -1)