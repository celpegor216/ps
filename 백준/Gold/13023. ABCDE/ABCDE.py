import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

result = 0

used = [0] * N

def dfs(now, cnt):
    global result

    if result:
        return

    if cnt == 5:
        result = 1
        return
    
    for item in lst[now]:
        if not used[item]:
            used[item] = 1
            dfs(item, cnt + 1)
            used[item] = 0

for n in range(N):
    dfs(n, 0)

print(result)