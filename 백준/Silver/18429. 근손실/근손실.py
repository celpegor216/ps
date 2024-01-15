N, K = map(int, input().split())
lst = sorted(map(int, input().split()), reverse=True)

result = 0

used = [0] * N

def dfs(level, now):    
    global result

    if level == N:
        result += 1
        return
    
    for n in range(N):
        if not used[n] and now - K + lst[n] >= 500:
            used[n] = 1
            dfs(level + 1, now - K + lst[n])
            used[n] = 0

dfs(0, 500)

print(result)