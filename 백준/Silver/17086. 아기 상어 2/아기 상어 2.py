from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [[-1] * M for _ in range(N)]
q = deque()

for n in range(N):
    for m in range(M):
        if lst[n][m] == 1:
            used[n][m] = 0
            q.append((n, m, 0))

while q:
    nowy, nowx, nowc = q.popleft()

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)):
        ny, nx = nowy + dy, nowx + dx
        if 0 <= ny < N and 0 <= nx < M and used[ny][nx] == -1:
            used[ny][nx] = nowc + 1
            q.append((ny, nx, nowc + 1))

result = 0
for n in range(N):
    for m in range(M):
        result = max(used[n][m], result)

print(result)