# 힌트: dp
# 해답: https://jshong1125.tistory.com/56

N, S, M = map(int, input().split())
lst = list(map(int, input().split()))

dp = [set() for _ in range(N + 1)]

dp[0] = [S]

for n in range(1, N + 1):
    if not dp[n - 1]:
        break
    for item in dp[n - 1]:
        if 0 <= item + lst[n - 1] <= M:
            dp[n].add(item + lst[n - 1])
        if 0 <= item - lst[n - 1] <= M:
            dp[n].add(item - lst[n - 1])

if not dp[-1]:
    print(-1)
else:
    print(max(dp[-1]))