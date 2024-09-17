N = 5
lst = [list(map(int, input().split())) for _ in range(N)]
sy, sx = map(int, input().split())

result = 0
def dfs(level, y, x, cnt):
    global result

    if cnt > 1 or result:
        result = 1
        return
    
    if level == 3:
        return
    
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and lst[ny][nx] != -1:
            tmp = lst[y][x]
            lst[y][x] = -1
            dfs(level + 1, ny, nx, cnt + lst[ny][nx])
            lst[y][x] = tmp

dfs(0, sy, sx, 0)

print(result)