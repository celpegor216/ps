# tree dp인데 풀이를 모르겠음
# 해답: https://tight-sleep.tistory.com/97

import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())
lst = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    lst[u].append(v)
    lst[v].append(u)

# dp[i][0]: i에 경찰서를 세우지 않은 경우
# dp[i][1]: i에 경찰서를 세운 경우
dp = [[0, 1] for _ in range(N + 1)]
used = [0] * (N + 1)

def dfs(now):
    for nxt in lst[now]:
        if not used[nxt]:
            used[nxt] = 1
            dfs(nxt)

            dp[now][0] += dp[nxt][1]
            dp[now][1] += min(dp[nxt])

used[1] = 1
dfs(1)

print(min(dp[1]))