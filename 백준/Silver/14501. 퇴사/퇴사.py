N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0

def dfs(level, total):
    global result
    
    if level == N:
        result = max(total, result)
        return

    if level > N: return
    
    dfs(level + 1, total)
    dfs(level + lst[level][0], total + lst[level][1])

dfs(0, 0)

print(result)