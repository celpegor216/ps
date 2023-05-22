N, M = map(int, input().split())
lst = sorted(map(int, input().split()))

used = [0] * N

def dfs(level, start, path):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, i + 1, path + [lst[i]])
            used[i] = 0

dfs(0, 0, [])