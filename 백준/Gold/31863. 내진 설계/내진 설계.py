N, M = map(int, input().split())
lst = [input() for _ in range(N)]

def find():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == '@':
                return i, j

sy, sx = find()

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

used = [[0] * M for _ in range(N)]
used[sy][sx] = 1

q = []
for dy, dx in directions:
    for i in range(1, 3):
        ny, nx = sy + dy * i, sx + dx * i
        if 0 <= ny < N and 0 <= nx < M:
            if lst[ny][nx] == '|':
                break

            if lst[ny][nx] in '.*' and used[ny][nx]:
                continue

            if lst[ny][nx] == '#' and used[ny][nx] == 2:
                continue

            used[ny][nx] += 1
            if lst[ny][nx] == '*' or (lst[ny][nx] == '#' and used[ny][nx] == 2):
                q.append((ny, nx))

while q:
    nq = []

    for y, x in q:
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if lst[ny][nx] == '|':
                    continue

                if lst[ny][nx] in '.*' and used[ny][nx]:
                    continue

                if lst[ny][nx] == '#' and used[ny][nx] == 2:
                    continue

                used[ny][nx] += 1
                if lst[ny][nx] == '*' or (lst[ny][nx] == '#' and used[ny][nx] == 2):
                    nq.append((ny, nx))

    q = nq

total = 0
broke_down = 0
for i in range(N):
    for j in range(M):
        if lst[i][j] == '*':
            total += 1
            if used[i][j]:
                broke_down += 1
        elif lst[i][j] == '#':
            total += 1
            if used[i][j] == 2:
                broke_down += 1

print(broke_down, total - broke_down)