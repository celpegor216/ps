import heapq

M, N = map(int, input().split())
lst = []
sy = sx = -1
rocks = []

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j].isdigit():
            tmp[j] = int(tmp[j])
        elif tmp[j] == 'T':
            sy, sx = i, j
            tmp[j] = 0
        elif tmp[j] == 'H':    # 구멍, 만나면 죽음
            tmp[j] = -1
        elif tmp[j] == 'R':    # 바위, 만나면 멈춤
            tmp[j] = -2
            rocks.append((i, j))
        elif tmp[j] == 'E':    # 탈출
            tmp[j] = -3
    lst.append(tmp)


edges = dict()


def find_edge(y, x):
    for dy, dx in directions:
        nt = lst[y][x]
        ny, nx = y + dy, x + dx
        while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] >= 0:
            nt += lst[ny][nx]
            ny += dy
            nx += dx

        # 절벽으로 떨어지거나 구멍에 빠진 경우
        if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == -1:
            continue

        if lst[ny][nx] == -2:
            ny -= dy
            nx -= dx

        if y == ny and x == nx:
            continue

        if not edges.get((y, x)):
            edges[(y, x)] = dict()
        edges[(y, x)][(ny, nx)] = nt


possibles = set()
possibles.add((sy, sx))
for y, x in rocks:
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] < 0:
            continue
        possibles.add((ny, nx))

for y, x in possibles:
    find_edge(y, x)


def find():
    q = []
    heapq.heappush(q, (0, sy, sx))
    results = [[21e8] * M for _ in range(N)]
    results[sy][sx] = 0

    while q:
        cost, y, x = heapq.heappop(q)

        if results[y][x] < cost:
            continue

        if lst[y][x] == -3:
            return cost - 3

        if not edges.get((y, x)):
            continue

        for nxt_pos, nxt_cost in edges[(y, x)].items():
            ny, nx = nxt_pos
            nxt = cost + nxt_cost - lst[ny][nx]

            if results[ny][nx] <= nxt:
                continue

            results[ny][nx] = nxt
            heapq.heappush(q, (nxt, ny, nx))


    return -1

print(find())