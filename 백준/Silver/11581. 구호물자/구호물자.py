N = int(input())
lst = [[]]
for _ in range(N - 1):
    _ = int(input())
    lst.append(list(map(int, input().split())))

used = [0] * (N + 1)
result = 0
def dfs(now):
    global result

    if now == N or result:
        return
    
    for nxt in lst[now]:
        if used[nxt]:
            result = 1
            return
        
        used[nxt] = 1
        dfs(nxt)
        used[nxt] = 0

used[1] = 1
dfs(1)

print('CYCLE' if result else 'NO CYCLE')