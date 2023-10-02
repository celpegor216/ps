# 한 L에서 연결된 L을 모두 찾고, 그 중 가장 멀리 떨어져 있는 L에서 다시 bfs -> 반례 존재
# 모든 L에서 bfs -> 시간초과 날 줄 알았는데 아니라고?

from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

result = 0
for n in range(N):
    for m in range(M):
        if lst[n][m] == 'L':
            used = [[0] * M for _ in range(N)]
            used[n][m] = 1
            q = deque()
            q.append((n, m, 0))

            while q:
                nowy, nowx, nowc = q.popleft()

                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ny, nx = nowy + dy, nowx + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == 'L':
                        q.append((ny, nx, nowc + 1))
                        used[ny][nx] = nowc + 1
                        result = max(result, nowc + 1)

print(result)