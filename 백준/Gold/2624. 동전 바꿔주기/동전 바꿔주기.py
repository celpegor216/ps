# dp인데 반례를 못 찾음
# 해답: https://one10004.tistory.com/281

T = int(input())
K = int(input())
coins = [list(map(int, input().split())) for _ in range(K)]

dp = [0] * (T + 1)
dp[0] = 1

for coin, cnt in coins:
    for t in range(T, 0, -1):
        for i in range(1, cnt + 1):
            if t - coin * i >= 0:
                dp[t] += dp[t - coin * i]

print(dp[-1])