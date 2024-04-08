rooms = list(map(int, input().split()))
N = rooms[-1]

result = False

used = [0] * 3

def dfs(now):
    global result

    if result:
        return
    
    if now == 0:
        result = True
        return
    
    for i in range(3):
        if not used[i]:
            used[i] = 1
            dfs(now % rooms[i])
            used[i] = 0

dfs(N)

print(1 if result else 0)