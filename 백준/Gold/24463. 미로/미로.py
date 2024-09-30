N, M = map(int, input().split())
lst = [input() for _ in range(N)]

edge_points = set()
for i in range(N):
    if lst[i][0] == '.':
        edge_points.add((i, 0))
    if lst[i][-1] == '.':
        edge_points.add((i, M - 1))
for j in range(M):
    if lst[0][j] == '.':
        edge_points.add((0, j))
    if lst[-1][j] == '.':
        edge_points.add((N - 1, j))

edge_points = list(edge_points)
sy, sx = edge_points[0]
ey, ex = edge_points[1]


def find():
    used = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    used[sy][sx] = [-2, -2]

    q = [(sy, sx)]

    while q:
        nq = []

        for y, x in q:
            if y == ey and x == ex:
                return used
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == '+' or used[ny][nx][0] != -1:
                    continue

                used[ny][nx] = [y, x]
                nq.append((ny, nx))

        q = nq


used = find()

result = [['@'] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j] == '+':
            result[i][j] = '+'

ny, nx = ey, ex
while not(ny == -2 and nx == -2):
    result[ny][nx] = '.'
    ny, nx = used[ny][nx]

for line in result:
    print(''.join(line))