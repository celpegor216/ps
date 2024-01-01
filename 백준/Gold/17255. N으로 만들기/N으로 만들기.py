N = input()

used = dict()

def dfs(now):
    if not used.get(now):
        if len(now) == 1:
            used[now] = 1
        else:
            if now[:-1] == now[1:]:
                used[now] = dfs(now[:-1])
            else:
                used[now] = dfs(now[:-1]) + dfs(now[1:])
    
    return used[now]

print(dfs(N))