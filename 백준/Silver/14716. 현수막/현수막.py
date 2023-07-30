from collections import deque

N, M = map(int, input().split())
lst = [input().split() for _ in range(N)]

used = [[0] * M for _ in range(N)]

cnt = 0
for n in range(N):
    for m in range(M):
        if lst[n][m] == '1' and not used[n][m]:
            cnt += 1

            q = deque()
            q.append((n, m))

            while q:
                y, x = q.popleft()

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == '1':
                        used[ny][nx] = 1
                        q.append((ny, nx))

print(cnt)