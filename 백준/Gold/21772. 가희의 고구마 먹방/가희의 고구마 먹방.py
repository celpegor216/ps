N, M, T = map(int, input().split())
lst = [list(input()) for _ in range(N)]


def find():
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'G':
                return i, j


sy, sx = find()

result = 0
def dfs(level, y, x, total):
    global result

    if level == T:
        result = max(result, total)
        return

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != '#':
            if lst[ny][nx] == 'S':
                lst[ny][nx] = '.'
                dfs(level + 1, ny, nx, total + 1)
                lst[ny][nx] = 'S'
            else:
                dfs(level + 1, ny, nx, total)

dfs(0, sy, sx, 0)

print(result)