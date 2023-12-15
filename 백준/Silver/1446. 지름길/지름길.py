N, D = map(int, input().split())
shortcuts = [list(map(int, input().split())) for _ in range(N)]
shortcuts.sort()

used = [0] * N

result = D
def dfs(now, total):
    global result

    if now <= D:
        result = min(result, total + D - now)
    
    if now >= D:
        return
    
    for n in range(N):
        if not used[n] and shortcuts[n][0] >= now:
            used[n] = 1
            dfs(shortcuts[n][1], total + shortcuts[n][2] + (shortcuts[n][0] - now))
            used[n] = 0

dfs(0, 0)

print(result)