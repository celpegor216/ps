C = int(input())

path = [0] * 11
def dfs(level):
    global result
    
    if level == 11:
        result = max(sum(path), result)
        return
    
    for i in range(11):
        if lst[level][i] and not path[i]:
            path[i] = lst[level][i]
            dfs(level + 1)
            path[i] = 0

for c in range(C):
    lst = [list(map(int, input().split())) for _ in range(11)]
    result = 0
    dfs(0)
    print(result)
    