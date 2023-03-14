L, C = map(int, input().split())
lst = sorted(input().split())

def dfs(level, next, path):
    if level == L:
        cnt = 0
        
        for item in 'aeiou':
            if item in path:
                cnt += 1
        
        if cnt > 0 and L - cnt > 1:
            print(path)
        return

    for i in range(next, C):
        dfs(level + 1, i + 1, path + lst[i])

dfs(0, 0, '')