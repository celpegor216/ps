# 반례 참고


import heapq


N, M = map(int, input().split())

# 출발점 C, 강아지 D, 도착점 E, 일반 바닥 F, 사다리 L, 아래가 뚫린 공간 X
lst = [list(input()) for _ in range(N)]

sy = sx = ey = ex = -1

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'C':
            lst[i][j] = 'F'
            sy, sx = i, j
        elif lst[i][j] == 'E':
            lst[i][j] = 'F'
            ey, ex = i, j


# 이동할 수 있는 모든 간선 만들어두기
edges = dict()
for i in range(N):
    for j in range(M):
        tmp = []

        if lst[i][j] == 'F':
            if j > 0 and lst[i][j - 1] != 'D':
                tmp.append((i, j - 1, 1))
            if j < M - 1 and lst[i][j + 1] != 'D':
                tmp.append((i, j + 1, 1))
            if i < N - 1 and lst[i + 1][j] == 'L':
                tmp.append((i + 1, j, 5))
            edges[(i, j)] = tmp

            y = i - 1
            while 0 <= y and lst[y][j] == 'X':
                edges[(y, j)] = [(i, j, 10)]
                y -= 1
        elif lst[i][j] == 'L':
            if j > 0 and lst[i][j - 1] != 'D':
                tmp.append((i, j - 1, 1))
            if j < M - 1 and lst[i][j + 1] != 'D':
                tmp.append((i, j + 1, 1))
            if i < N - 1 and lst[i + 1][j] == 'L':
                tmp.append((i + 1, j, 5))
            if i > 0 and lst[i - 1][j] != 'D':
                tmp.append((i - 1, j, 5))
            edges[(i, j)] = tmp

            y = i - 1
            while 0 <= y and lst[y][j] == 'X':
                edges[(y, j)] = [(i, j, 10)]
                y -= 1


def find(sy, sx, ey, ex):
    used = [[21e8] * M for _ in range(N)]
    used[sy][sx] = 0

    q = []
    heapq.heappush(q, (0, sy, sx))

    while q:
        cnt, y, x = heapq.heappop(q)

        if used[y][x] < cnt:
            continue

        if y == ey and x == ex:
            return cnt

        if edges.get((y, x)):
            for ny, nx, c in edges[(y, x)]:
                nc = cnt + c
                if used[ny][nx] > nc:
                    used[ny][nx] = nc
                    heapq.heappush(q, (nc, ny, nx))

    return 'dodo sad'


print(find(sy, sx, ey, ex))