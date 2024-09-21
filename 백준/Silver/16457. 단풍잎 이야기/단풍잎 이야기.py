N, M, K = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(M)]

result = 0
def dfs(level, start, now):
    global result

    if level == N:
        completed_quests = [0] * M

        for m in range(M):
            for skill in lst[m]:
                if skill not in now:
                    break
            else:
                completed_quests[m] = 1
        
        result = max(result, sum(completed_quests))
        return
    
    for n in range(start, N * 2):
        dfs(level + 1, n + 1, now + [n + 1])

dfs(0, 0, [])

print(result)