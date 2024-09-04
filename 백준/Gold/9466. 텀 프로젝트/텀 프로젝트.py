# 힌트: dfs

import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

T = int(input())

def dfs(now):
    if used[now] == 1:
        return now
    elif result[now]:
        return -1

    used[now] = 1
    cycle_num = dfs(lst[now])
    used[now] = 0

    if cycle_num == -1:
        result[now] = -1
        return -1
    elif cycle_num == now:
        result[now] = 1
        return -1
    else:
        result[now] = 1
        return cycle_num


for _ in range(T):
    N = int(input())
    lst = list(map(lambda x: int(x) - 1, input().split()))
    used = [0] * N
    result = [0] * N

    for n in range(N):
        if result[n]:
            continue
        dfs(n)

    print(result.count(-1))