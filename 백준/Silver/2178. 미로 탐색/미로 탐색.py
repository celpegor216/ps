from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

q = deque()
q.append((0, 0))
used = [[0] * M for _ in range(N)]
used[0][0] = 1

result = 0

while q:
    y, x = q.popleft()

    if y == N - 1 and x == M - 1:
        result = used[y][x]
        break

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == '1' and not used[ny][nx]:
            q.append((ny, nx))
            used[ny][nx] = used[y][x] + 1

print(result)