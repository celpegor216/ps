from collections import deque

N, M, K = map(int, input().split())
lst = [[0] * M for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())

    lst[y - 1][x - 1] = 1

used = [[0] * M for _ in range(N)]

result = 0

for n in range(N):
    for m in range(M):
        if lst[n][m] and not used[n][m]:
            used[n][m] = 1

            q = deque()
            q.append((n, m))
            cnt = 0

            while q:
                y, x = q.popleft()

                cnt += 1

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = dy + y, dx + x
                    if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] and not used[ny][nx]:
                        used[ny][nx] = 1
                        q.append((ny, nx))
            
            result = max(result, cnt)

print(result)