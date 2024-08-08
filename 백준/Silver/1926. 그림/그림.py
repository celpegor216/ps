from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]

result_cnt = 0
result_max = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] and not used[i][j]:
            used[i][j] = 1

            q = deque()
            q.append((i, j))

            result_cnt += 1
            cnt = 0

            while q:
                y, x = q.popleft()

                cnt += 1

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx]:
                        used[ny][nx] = 1
                        q.append((ny, nx))

            result_max = max(result_max, cnt)

print(result_cnt)
print(result_max)