N = int(input())

used = [0] * N

def dfs(level, path):
    if level == N:
        print(*path)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = 1
            dfs(level + 1, path + [i + 1])
            used[i] = 0

dfs(0, [])