N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 21e8

def dfs(level, next, path):
    global result
    
    if level == N // 2:
        return
    
    for i in range(next, N):
        temp = path + [i]
        
        total_s = 0
        for a in temp:
            for b in temp:
                total_s += lst[a][b]
        
        not_temp = [x for x in range(N) if x not in temp]
        total_l = 0
        for a in not_temp:
            for b in not_temp:
                total_l += lst[a][b]
        
        result = min(result, abs(total_s - total_l))
        
        dfs(level + 1, i + 1, temp)

dfs(0, 0, [])

print(result)