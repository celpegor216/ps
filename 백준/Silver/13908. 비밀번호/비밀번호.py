N, M = map(int, input().split())

if M:
    lst = list(map(int, input().split()))
else:
    lst = []

result = 0
def dfs(level, path):
    global result

    if level == N:
        flag = 0

        for item in lst:
            if item not in path:
                flag = 1
                break
        
        if not flag:
            result += 1
        return
    
    for i in range(10):
        dfs(level + 1, path + [i])

dfs(0, [])

print(result)