N, M = map(int, input().split())

def dfs(level, start, path):
    if level == M:
        print(*path)
        return

    for i in range(start + 1, N + 1):
        dfs(level + 1, i, path + [i])

dfs(0, 0, [])