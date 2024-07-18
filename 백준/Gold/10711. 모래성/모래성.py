# 해답: https://paris-in-the-rain.tistory.com/122

from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
used = [[0] * M for _ in range(N)]

q = deque()

for n in range(N):
    for m in range(M):
        if lst[n][m] != '.':
            lst[n][m] = int(lst[n][m])
        else:
            lst[n][m] = 0
            q.append((n, m))

result = 0

while q:
    n, m = q.popleft()

    for dy, dx in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
        ny, nx = n + dy, m + dx

        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx]:
            lst[ny][nx] -= 1

            if not lst[ny][nx]:
                q.append((ny, nx))
                used[ny][nx] = used[n][m] + 1
                result = max(result, used[ny][nx])

print(result)    
