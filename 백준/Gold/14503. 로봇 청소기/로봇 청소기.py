N, M = map(int, input().split())
y, x, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * M for _ in range(N)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 0
while 1:
    if not used[y][x]:
        used[y][x] = 1
        result += 1
    
    flag = 0
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and not used[ny][nx]:
            flag = 1
            break
    
    if not flag:
        dy, dx = directions[d]
        ny, nx = y - dy, x - dx
        
        if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx]:
            y, x = ny, nx
        else:
            break
    else:
        d = d - 1 if d > 0 else 3
        dy, dx = directions[d]
        ny, nx = y + dy, x + dx
        
        if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and not used[ny][nx]:
            y, x = ny, nx

print(result)