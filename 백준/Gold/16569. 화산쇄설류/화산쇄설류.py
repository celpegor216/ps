# 반례 참고


transform = lambda x: int(x) - 1

N, M, V = map(int, input().split())
sy, sx = map(transform, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

volcano = []
for _ in range(V):
    y, x, t = map(transform, input().split())
    lst[y][x] = -1
    volcano.append((t + 1, y, x))

volcano.sort()
v_idx = 0

volcano_q = []
person_q = [(sy, sx)]
used[sy][sx] = 1

maxv = lst[sy][sx]
maxtime = 0
time = 0

while person_q:
    # 화산 먼저 움직이기
    volcano_nq = []

    while v_idx < V and volcano[v_idx][0] == time:
        y, x = volcano[v_idx][1:]
        volcano_q.append((y, x))
        v_idx += 1

    for y, x in volcano_q:
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and used[ny][nx] != 2:
                used[ny][nx] = 2
                volcano_nq.append((ny, nx))

    volcano_q = volcano_nq

    # 사람 움직이기
    person_nq = []

    for y, x in person_q:
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] >= 0:
                if lst[ny][nx] > maxv:
                    maxv = lst[ny][nx]
                    maxtime = time + 1
                used[ny][nx] = 1
                person_nq.append((ny, nx))

    person_q = person_nq

    time += 1


print(maxv, maxtime)