K = int(input())
lst = input().split()

min_v = 21e10
max_v = 0

def dfs(level, path):
    global min_v, max_v
    
    if level == K + 1:
        flag = 0
        
        for i in range(1, K + 1):
            if (lst[i - 1] == '>' and path[i - 1] < path[i]) or (lst[i - 1] == '<' and path[i - 1] > path[i]):
                flag = 1
                break
        
        if not flag:
            min_v = min(min_v, int(path))
            max_v = max(max_v, int(path))
        
        return
    
    for i in range(10):
        if str(i) not in path:
            dfs(level + 1, path + str(i))
        
dfs(0, '')

print(max_v)
print(min_v if len(str(min_v)) == K + 1 else '0' + str(min_v))