N, M = map(int, input().split())
lst = sorted(map(int, input().split()))

def dfs(level, path):
    if level == M:
        print(*path)
        return

    for i in range(N):
        dfs(level + 1, path + [lst[i]])

dfs(0, [])