N, M = map(int, input().split())

lst = [list(map(int, input().split(' '))) for _ in range(N)]

result = 0

def dfs(level, total, path):
    global result

    if level == 4:
        if result < total:
            result = total
        return

    for y, x in path:
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in path:
                dfs(level + 1, total + lst[ny][nx], path + [(ny, nx)])

for n in range(N):
    for m in range(M):
        dfs(1, lst[n][m], [(n, m)])

print(result)