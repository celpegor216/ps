from collections import deque

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

q = deque()
used = [[0] * M for _ in range(N)]
cnt = 0

for n in range(N):
    for m in range(M):
        if lst[n][m] == 1:
            q.append((n, m))
            used[n][m] = 1
        elif lst[n][m] == 0:
            cnt += 1

result = -1
while q:
    length = len(q)
    for _ in range(length):
        y, x = q.popleft()

        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == 0:
                q.append((ny, nx))
                used[ny][nx] = 1
                cnt -= 1

    result += 1

if cnt:
    result = -1

print(result)