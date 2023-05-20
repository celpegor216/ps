N, M = map(int, input().split())

def dfs(level, path):
    if level == M:
        print(*path)
        return
    
    for i in range(1, N + 1):
        dfs(level + 1, path + [i])
        
dfs(0, [])