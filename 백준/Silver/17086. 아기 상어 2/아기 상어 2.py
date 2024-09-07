from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

q = deque()
used = [[21e8] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if lst[i][j]:
            q.append((i, j, 0))
            used[i][j] = 0

directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

while q:
    y, x, cnt = q.popleft()

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and used[ny][nx] > cnt + 1:
            used[ny][nx] = cnt + 1
            q.append((ny, nx, cnt + 1))

print(max([max(line) for line in used]))