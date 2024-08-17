# 시작할 때 1번 나무 아래에 위치해있음

T, W = map(int, input().split())
lst = [int(input()) for _ in range(T)]

dp = [[[0] * 2 for _ in range(W + 1)] for _ in range(T)]

if lst[0] == 1:
    dp[0][0][0] = 1
else:
    dp[0][1][1] = 1

for t in range(1, T):
    dp[t][0][0] = dp[t - 1][0][0]
    if lst[t] == 1:
        dp[t][0][0] += 1

    for w in range(1, W + 1):
        if w > t + 1:
            break

        dp[t][w][lst[t] - 1] += 1
        for i in range(2):
            dp[t][w][i] += max(dp[t - 1][w][i], dp[t - 1][w - 1][i ^ 1])

print(max([max(dp[-1][w]) for w in range(W + 1)]))