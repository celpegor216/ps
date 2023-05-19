N, M = map(int, input().split())

used = [0] * (N + 1)

def dfs(level, path):
    if level == M:
        print(*path)
        return
    
    for i in range(1, N + 1):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, path + [i])
            used[i] = 0

dfs(0, [])