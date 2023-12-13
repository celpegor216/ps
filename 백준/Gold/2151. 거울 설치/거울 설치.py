from collections import deque

N = int(input())
lst = [input() for _ in range(N)]

doors = []
mirrors = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == '#':
            doors.append((i, j))
        elif lst[i][j] == '!':
            mirrors.append((i, j))

q = deque()
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
used = [[[0, 0] for _ in range(N)] for _ in range(N)]
used[doors[0][0]][doors[0][1]] = [1, 1]

result = -1
for i in range(4):
    ny, nx = doors[0][0] + d[i][0], doors[0][1] + d[i][1]
    while 0 <= ny < N and 0 <= nx < N and lst[ny][nx] != '*':
        if (ny, nx) in mirrors and not used[ny][nx][i % 2]:
            q.append((ny, nx, i % 2, 1))
            used[ny][nx][i % 2] = 1
        elif lst[ny][nx] == '#':
            result = 0
            break
        ny += d[i][0]
        nx += d[i][1]

    if result != -1:
        q = []
        break

def bfs():
    while q:
        y, x, direction, cnt = q.popleft()

        for i in range(2):
            n = (direction + i * 2 + 1) % 4
            ny, nx = y + d[n][0], x + d[n][1]
            while 0 <= ny < N and 0 <= nx < N and lst[ny][nx] != '*':
                if (ny, nx) in mirrors and not used[ny][nx][n % 2]:
                    q.append((ny, nx, n % 2, cnt + 1))
                    used[ny][nx][n % 2] = cnt + 1
                elif lst[ny][nx] == '#' and not used[ny][nx][n % 2]:
                    return cnt
                ny += d[n][0]
                nx += d[n][1]

if result == -1:
    result = bfs()

print(result)