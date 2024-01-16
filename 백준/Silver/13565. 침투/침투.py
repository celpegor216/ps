from collections import deque

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

q = deque()
used = [[0] * M for _ in range(N)]

result = 'NO'

def bfs(m):
    global result

    used[0][m] = 1
    q.append((0, m))

    while q:
        y, x = q.popleft()

        if y == N - 1:
            result = 'YES'
            return
        
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == '0':
                used[ny][nx] = 1
                q.append((ny, nx))

for m in range(M):
    if not used[0][m] and lst[0][m] == '0':
        bfs(m)

    if result == 'YES':
        break

print(result)