N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
used = [0] * (N + 1)

result = 1

def dfs(level, cnt):
    global result

    if cnt < N:
        result = max(result, cnt + 1)
    else:
        result = max(result, cnt)
    
    if level == M:
        return
    
    for i in range(level, M):
        if not used[lst[i][0]] and not used[lst[i][1]]:
            used[lst[i][0]] = 1
            used[lst[i][1]] = 1
            dfs(i + 1, cnt + 2)
            used[lst[i][0]] = 0
            used[lst[i][1]] = 0

dfs(0, 0)

print(result)