def solution(n, computers):
    used = [-1] * n
    
    def dfs(start, now):
        nonlocal used
        
        for i in range(n):
            if computers[now][i] and used[i] == -1:
                used[i] = start
                dfs(start, i)
    
    for i in range(n):
        dfs(i, i)
    
    print(used)
    
    return len(set(used))