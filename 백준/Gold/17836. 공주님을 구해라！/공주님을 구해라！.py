from collections import deque

N, M, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
gy = gx = -1

for n in range(N):
    if gy != -1:
        break

    for m in range(M):
        if lst[n][m] == 2:
            gy = n
            gx = m
            break

q = deque()
used = [[0] * M for _ in range(N)]

q.append((0, 0))
used[0][0] = 1

while q:
    y, x = q.popleft()

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] != 1:
            q.append((ny, nx))
            used[ny][nx] = used[y][x] + 1

result_g = used[gy][gx] + N - gy - 1 + M - gx - 1 - 1 if used[gy][gx] else 21e8
result_ng = used[-1][-1] - 1 if used[-1][-1] else 21e8
result = min(result_g, result_ng)

if result > T:
    print('Fail')
else:
    print(result)