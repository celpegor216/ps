N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

result = -21e8
def dfs(level, start, selected):
    global result

    if level == K:
        total = 0
        for i in range(K - 1):
            for j in range(i + 1, K):
                total += lst[selected[i]][selected[j]]
        result = max(result, total)
        return
    
    for i in range(start, N - (K - level) + 1):
        dfs(level + 1, i + 1, selected + [i])

dfs(0, 0, [])

print(result)