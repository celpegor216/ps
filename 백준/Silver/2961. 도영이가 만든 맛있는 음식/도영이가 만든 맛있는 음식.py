import math

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = math.inf
used = [0] * N

def dfs(level, nows, nowb):
    global result
    
    if level == N:
        if sum(used) > 0:
            result = min(result, abs(nows - nowb))
        return
    
    dfs(level + 1, nows, nowb)
    used[level] = 1
    dfs(level + 1, nows * lst[level][0], nowb + lst[level][1])

dfs(0, 1, 0)

print(result)