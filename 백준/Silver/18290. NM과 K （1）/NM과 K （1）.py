N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

used = [[0] * M for _ in range(N)]
result = -21e8
def dfs(level, total, k):
    global result

    if k == K:
        result = max(result, total)
        return

    if level == N * M:
        return
    
    y, x = level // M, level % M

    if not used[y][x]:
        for dy, dx in ((0, 0), (0, -1), (-1, 0), (0, 1), (1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                used[ny][nx] += 1
        
        dfs(level + 1, total + lst[y][x], k + 1)

        for dy, dx in ((0, 0), (0, -1), (-1, 0), (0, 1), (1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                used[ny][nx] -= 1
    
    dfs(level + 1, total, k)

dfs(0, 0, 0)

print(result)