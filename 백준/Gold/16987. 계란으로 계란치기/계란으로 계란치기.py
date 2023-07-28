N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0

def dfs(level, path):
    global result

    if level == N:
        cnt = 0

        for item in path:
            if item <= 0:
                cnt += 1

        result = max(result, cnt)
        return
    
    for i in range(N):
        if level != i:
            if path[level] > 0 and path[i] > 0:
                path[i] -= lst[level][1]
                path[level] -= lst[i][1]
                dfs(level + 1, path)
                path[i] += lst[level][1]
                path[level] += lst[i][1]
            else:
                dfs(level + 1, path)

path = [x[0] for x in lst]
dfs(0, path)

print(result)