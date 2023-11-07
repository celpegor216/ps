from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

places = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            places.append((i, j))

length = len(places)
used = [0] * length

result = 21e8

def dfs(level, now):
    global M, result

    if level == M:
        q = deque()
        visited = [[0] * N for _ in range(N)]
        
        for i in range(length):
            if used[i]:
                y, x = places[i]
                q.append((y, x, 1))
                visited[y][x] = 1
        
        while q:
            nowy, nowx, nowc = q.popleft()

            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ny, nx = nowy + dy, nowx + dx
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and lst[ny][nx] != 1:
                    q.append((ny, nx, nowc + 1))
                    visited[ny][nx] = nowc + 1
        
        flag = 0
        maxv = 0

        for i in range(N):
            if flag:
                break

            for j in range(N):
                if lst[i][j] != 1:
                    if visited[i][j] == 0:
                        flag = 1
                        break
                    else:
                        maxv = max(maxv, visited[i][j])

        if not flag:
            result = min(result, maxv)

        return

    for i in range(now + 1, length):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, i)
            used[i] = 0

dfs(0, -1)

if result == 21e8:
    print(-1)
else:
    print(result - 1)