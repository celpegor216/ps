N, K = map(int, input().split())

cnt = 0
result = ''

def dfs(path, total):
    global cnt, result
    
    if result:
        return

    if total == N:
        cnt += 1
        
        if cnt == K:
            result = '+'.join(map(str, path))
        
        return

    for i in range(1, 4):
        if total + i > N:
            break
        dfs(path + [i], total + i)

dfs([], 0)

print(result if result else -1)