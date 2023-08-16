N, M = map(int, input().split())
lst = sorted(map(int, input().split()))
used = []

def dfs(level, path, now):
    if level == M:
        print(*path)
        return
    
    for i in range(now, N):
        if path + [lst[i]] not in used:
            used.append(path + [lst[i]])
            dfs(level + 1, path + [lst[i]], i + 1)

dfs(0, [], 0)