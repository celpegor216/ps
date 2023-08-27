N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

used = [0] * (N + 1)

result = 0
def dfs(level, now, path):
    global result
    if level == 3:
        result += 1
        return
    
    for i in range(now + 1, N + 1):
        if not used[i]:
            flag = 0

            for item in path:
                if item in lst[i]:
                    flag = 1
                    break
            
            if not flag:
                used[i] = 1
                dfs(level + 1, i, path + [i])
                used[i] = 0

dfs(0, 0, [])

print(result)