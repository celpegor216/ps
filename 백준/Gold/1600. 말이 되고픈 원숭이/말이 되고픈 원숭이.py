from collections import deque

K = int(input())
M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

q = deque()
used = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]

q.append((0, 0, 1, 0))
used[0][0][0] = 1

d1 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d2 = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

while q:
    y, x, cnt, k = q.popleft()

    if y == N - 1 and x == M - 1:
        continue

    for dy, dx in d1:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and not used[ny][nx][k]:
            q.append((ny, nx, cnt + 1, k))
            used[ny][nx][k] = cnt + 1
    
    if k < K:
        for dy, dx in d2:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and not used[ny][nx][k + 1]:
                q.append((ny, nx, cnt + 1, k + 1))
                used[ny][nx][k + 1] = cnt + 1

result = 21e8

for item in used[-1][-1]:
    if item and result > item:
        result = item

if result == 21e8:
    print(-1)
else:
    print(result - 1)