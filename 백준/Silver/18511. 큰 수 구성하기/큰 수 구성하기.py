N, K = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
def dfs(now):
    global result

    if result < now <= N:
        result = now
    
    if now >= N:
        return
    
    for k in range(K):
        dfs(now * 10 + lst[k])

dfs(0)

print(result)