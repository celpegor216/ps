N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

result = 21e8
used = [0] * N
def dfs(level, start, now, total):
    global result

    if level == N - 1:
        if lst[now][start] > 0 and result > total + lst[now][start]:
            result = total + lst[now][start]
        return
    
    for n in range(N):
        if lst[now][n] > 0 and not used[n]:
            used[n] = 1
            dfs(level + 1, start, n, total + lst[now][n])
            used[n] = 0

for start in range(N):
    used[start] = 1
    dfs(0, start, start, 0)
    used[start] = 0

print(result)