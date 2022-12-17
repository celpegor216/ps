N, M = map(int, input().split())

lst = sorted(map(int, input().split()))

def dfs(level, before, path):
    if level == M:
        print(*path)
        return

    for i in range(before, N):
        dfs(level + 1, i, path + [lst[i]])

dfs(0, 0, [])