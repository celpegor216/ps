from collections import deque


def transform(x):
    return int(x) - 1

N, K, R = map(int, input().split())

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

adj = [[[1] * 4 for _ in range(N)] for _ in range(N)]

for _ in range(R):
    ay, ax, by, bx = map(transform, input().split())

    # a가 왼쪽, b가 오른쪽인 경우
    if ay == by and ax == bx - 1:
        adj[ay][ax][0] = 0
        adj[by][bx][2] = 0
    # a가 오른쪽, b가 왼쪽인 경우
    elif ay == by and ax == bx + 1:
        adj[ay][ax][2] = 0
        adj[by][bx][0] = 0
    # a가 위쪽, b가 아래쪽인 경우
    elif ax == bx and ay == by - 1:
        adj[ay][ax][1] = 0
        adj[by][bx][3] = 0
    # a가 아래쪽, b가 위쪽인 경우
    elif ax == bx and ay == by + 1:
        adj[ay][ax][3] = 0
        adj[by][bx][1] = 0

cows = [list(map(transform, input().split())) for _ in range(K)]

groups = [[i * N + j for j in range(N)] for i in range(N)]
used = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if used[i][j]:
            continue

        q = deque()
        q.append((i, j))

        used[i][j] = 1

        while q:
            y, x = q.popleft()

            for d in range(4):
                if not adj[y][x][d]:
                    continue

                dy, dx = directions[d]
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not used[ny][nx]:
                    used[ny][nx] = 1
                    q.append((ny, nx))
                    groups[ny][nx] = groups[i][j]

result = 0
for i in range(K - 1):
    for j in range(i + 1, K):
        if groups[cows[i][0]][cows[i][1]] != groups[cows[j][0]][cows[j][1]]:
            result += 1

print(result)