N = 5
lst = [input().split() for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

used = set()

def dfs(level, y, x, total):
    if level == 5:
        used.add(total)
        return
    
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N:
            dfs(level + 1, ny, nx, total + lst[ny][nx])

for i in range(N):
    for j in range(N):
        dfs(0, i, j, lst[i][j])

print(len(used))