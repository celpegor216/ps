import sys
input = sys.stdin.readline

def dfs(now):
    maxv = 0

    for parent in parents[now]:
        if used[parent] == -1:
            used[parent] = dfs(parent)
        maxv = max(maxv, used[parent])
    
    return maxv + lst[now]

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    parents = [[] for _ in range(N + 1)]

    for k in range(K):
        a, b = map(int, input().split())
        parents[b].append(a)
    
    W = int(input())

    used = [-1] * (N + 1)

    for n in range(1, N + 1):
        if not parents[n]:
            used[n] = lst[n]

    result = dfs(W)
    
    print(result)