# 해답: https://myjamong.tistory.com/313

N = int(input())
lst = [int(input()) for _ in range(N)]

dp = [0] * N
dp[0] = lst[0]

if N > 1:
    dp[1] = lst[0] + lst[1]

if N > 2:
    dp[2] = max(dp[1], lst[0] + lst[2], lst[1] + lst[2])

if N > 3:
    for i in range(3, N):
        # 지금 잔 수에서 2잔을 마셨을 때 최대 -> 지금 잔 + 이전 잔 + 하나 건너 뛰고 이전전전 잔
        # 지금 잔 수에서 1잔을 마셨을 때 최대 -> 지금 잔 + 하나 건너 뛰고 이전전 잔
        # 지금 잔 수에서 안 마셨을 때 최대 -> 이전 잔
        dp[i] = max(lst[i] + lst[i - 1] + dp[i - 3], lst[i] + dp[i - 2], dp[i - 1])

print(dp[-1])