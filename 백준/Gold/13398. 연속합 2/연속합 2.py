N = int(input())
lst = list(map(int, input().split()))

dp = [[0] * N for _ in range(2)]
dp[0][0] = lst[0]

result = min(lst)
for n in range(1, N):
    # 제거 X -> 이전 제거 X + 지금, 지금
    dp[0][n] = max(dp[0][n - 1] + lst[n], lst[n])
    # 제거 O -> 이전 제거 X, 이전 제거 O + 지금
    dp[1][n] = max(dp[0][n - 1], dp[1][n - 1] + lst[n])

    result = max(result, dp[0][n], dp[1][n])

print(result)