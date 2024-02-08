N = int(input())
lst = list(map(int, input().split()))

result = 0
used = [0] * N

def dfs(level, now):
    global result

    if level == N:
        tmp = 0
        for n in range(N - 1):
            tmp += abs(now[n] - now[n + 1])
        result = max(result, tmp)
        return
    
    for n in range(N):
        if not used[n]:
            used[n] = 1
            dfs(level + 1, now + [lst[n]])
            used[n] = 0

dfs(0, [])

print(result)