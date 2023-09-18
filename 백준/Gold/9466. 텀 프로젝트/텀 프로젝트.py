# 해답: https://aia1235.tistory.com/47

import sys
sys.setrecursionlimit(10 ** 6)

T = int(input())

def dfs(now):
    global result

    used[now] = 1
    path.append(now)

    if not used[lst[now]]:
        dfs(lst[now])
    else:
        if lst[now] in path:
            result -= (len(path) - path.index(lst[now])) 
        return

for t in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    used = [0] * (N + 1)

    result = N

    for n in range(1, N + 1):
        if not used[n]:
            path = []
            dfs(n)
    
    print(result)