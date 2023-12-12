# 해답: https://kimmeh1.tistory.com/550

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
lst = [[] for _ in range(N + 1)]

for n in range(N - 1):
    a, b = map(int, input().split())

    lst[a].append(b)
    lst[b].append(a)

# 지금 노드가 얼리어답터일 경우 최소 정점의 수 / 아닐 경우 최소 정점의 수
dp = [[0, 0] for _ in range(N + 1)]
used = [0] * (N + 1)

def dfs(now):
    used[now] = 1
    dp[now][0] = 1
    for child in lst[now]:
        if not used[child]:
            dfs(child)

            # 지금 노드가 얼리어답터면 자식이 반드시 얼리어답터여야 하는 건 아님
            dp[now][0] += min(dp[child])

            # 지금 노드가 얼리어답터가 아니라면 자식이 반드시 얼리어답터여야 함
            dp[now][1] += dp[child][0]

dfs(1)

print(min(dp[1]))