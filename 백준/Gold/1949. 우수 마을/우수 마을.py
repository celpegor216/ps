# 해답: https://velog.io/@heyksw/Python-%EB%B0%B1%EC%A4%80-gold-1949-%EC%9A%B0%EC%88%98-%EB%A7%88%EC%9D%84

import sys
sys.setrecursionlimit(10 ** 5)

N = int(input())
towns = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
used = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    used[now] = 1

    # now를 루트로 하는 서브트리에서, now가 우수 마을로 선정되었을 때 최댓값
    dp[now][1] += towns[now]

    for child in graph[now]:
        if not used[child]:
            dfs(child)

            # now를 넣지 않았다면 child를 넣을 수도 안 넣을 수도 있음
            dp[now][0] += max(dp[child])

            # now를 넣었다면 child를 넣을 수 없음
            dp[now][1] += dp[child][0]

dfs(1)

print(max(dp[1]))