from collections import deque

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
viruses = []

for i in range(N):
    for j in range(N):
        if lst[i][j] == 2:
            viruses.append((i, j))

length = len(viruses)
used = [0] * length
result = 21e8

def check():
    q = deque()
    visited = [[0] * N for _ in range(N)]

    for i in range(length):
        if used[i]:
            q.append((*viruses[i], 0))
            visited[viruses[i][0]][viruses[i][1]] = 1
    
    time = 0

    while q:
        nowy, nowx, nowc = q.popleft()
    
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = nowy + dy, nowx + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if lst[ny][nx] == 0:
                    visited[ny][nx] = 1
                    q.append((ny, nx, nowc + 1))
                    time = max(time, nowc + 1)
                elif lst[ny][nx] == 2:
                    visited[ny][nx] = 1
                    q.append((ny, nx, nowc + 1))
    
    if time > result:
        return 21e8

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and lst[i][j] == 0:
                return 21e8
    
    return time
            

def compose(level, start):
    global result

    if level == M:
        result = min(result, check())
        return
    
    for i in range(start, length):
        if not used[i]:
            used[i] = 1
            compose(level + 1, i + 1)
            used[i] = 0

compose(0, 0)

if result != 21e8:
    print(result)
else:
    print(-1)