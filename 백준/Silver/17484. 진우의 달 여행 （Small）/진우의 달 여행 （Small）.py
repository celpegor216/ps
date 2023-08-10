N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 21e8
directions = [-1, 0, 1]

def dfs(level, x, before, total):
    global result

    if level == N:
        result = min(result, total)
        return
    
    for i in range(3):
        temp = x + directions[i]
        if i != before and 0 <= temp < M:
            dfs(level + 1, temp, i, total + lst[level][temp])

for m in range(M):
    dfs(1, m, -1, lst[0][m])

print(result)