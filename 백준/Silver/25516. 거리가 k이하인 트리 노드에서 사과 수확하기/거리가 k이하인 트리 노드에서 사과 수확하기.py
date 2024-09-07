import sys
sys.setrecursionlimit(10 ** 5)


N, K = map(int, input().split())
children = [[] for _ in range(N)]
for _ in range(N - 1):
    p, c = map(int, input().split())
    children[p].append(c)
has_apple = list(map(int, input().split()))

result = 0
def dfs(level, now):
    global result

    if has_apple[now]:
        result += 1
    
    if level == K:
        return
    
    for child in children[now]:
        dfs(level + 1, child)

dfs(0, 0)

print(result)