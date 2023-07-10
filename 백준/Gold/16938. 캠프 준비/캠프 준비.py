N, L, R, X = map(int, input().split())
lst = sorted(map(int, input().split()))

result = 0

def dfs(level, now, total, minv, maxv):
    global result

    if level > 1:
        if L <= total <= R and maxv - minv >= X:
            result += 1

    if level == N:
        return
    
    for i in range(now, N):
        if level == 0:
            dfs(level + 1, i + 1, total + lst[i], lst[i], 0)
        else:
            dfs(level + 1, i + 1, total + lst[i], minv, lst[i])

dfs(0, 0, 0, 0, 0)

print(result)