from collections import deque

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

maxv = 0
for line in lst:
    maxv = max(maxv, max(line))

result = 1

for i in range(1, maxv):
    q = deque()
    used = [[0] * N for _ in range(N)]
    cnt = 0

    for n in range(N):
        for m in range(N):
            if lst[n][m] > i and not used[n][m]:
                q.append((n, m))
                used[n][m] = 1
                cnt += 1

                while q:
                    y, x = q.popleft()

                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = y + dy, x + dx

                        if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and lst[ny][nx] > i:
                            q.append((ny, nx))
                            used[ny][nx] = 1

    result = max(result, cnt)

print(result)