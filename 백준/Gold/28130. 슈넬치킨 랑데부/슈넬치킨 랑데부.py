import sys
input = sys.stdin.readline


N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

ay = ax = by = bx = -1

for i in range(N):
    for j in range(M):
        if lst[i][j] == 'A':
            lst[i][j] = '.'
            ay, ax = i, j
        elif lst[i][j] == 'B':
            lst[i][j] = '.'
            by, bx = i, j

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 선우는 연병장의 가장자리 중 어딘가에서 출발해 1분마다 시계방향으로 이동
outlines = []
for j in range(M - 1):
    outlines.append((0, j))
for i in range(N - 1):
    outlines.append((i, M - 1))
for j in range(M - 1, 0, -1):
    outlines.append((N - 1, j))
for i in range(N - 1, 0, -1):
    outlines.append((i, 0))
cycle = len(outlines)

a_idx = -1
for i in range(cycle):
    if outlines[i] == (by, bx):
        a_idx = i
        break


outlines_dict = dict()
for i in range(cycle):
    outlines_dict[outlines[a_idx]] = i
    a_idx = (a_idx + 1) % cycle


def find(sy, sx):
    used = [[21e8] * M for _ in range(N)]
    used[sy][sx] = 0

    q = [(sy, sx)]

    time = 0
    while q:
        nq = []

        for y, x in q:
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                nt = time + 1
                if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '.' and used[ny][nx] > nt:
                    used[ny][nx] = nt
                    nq.append((ny, nx))

        q = nq
        time += 1

    result = 21e8
    for (y, x), time in outlines_dict.items():
        if used[y][x] != 21e8 and used[y][x] % cycle == time:
            result = min(result, used[y][x])

    return -1 if result == 21e8 else result


print(find(ay, ax))