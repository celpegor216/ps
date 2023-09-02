from collections import deque

N, L, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while 1:
    groups = []
    used = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not used[i][j]:
                q = deque()
                q.append((i, j))
                group = [(i, j)]
                used[i][j] = 1

                while q:
                    nowy, nowx = q.popleft()
                    
                    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ny, nx = nowy + dy, nowx + dx
                        if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and L <= abs(lst[nowy][nowx] - lst[ny][nx]) <= R:
                            group.append((ny, nx))
                            q.append((ny, nx))
                            used[ny][nx] = 1
                
                if len(group) > 1:
                    groups.append(group)
    
    if not groups: break

    for group in groups:
        middle = sum([lst[g[0]][g[1]] for g in group]) // len(group)

        for y, x in group:
            lst[y][x] = middle
    
    cnt += 1

print(cnt)