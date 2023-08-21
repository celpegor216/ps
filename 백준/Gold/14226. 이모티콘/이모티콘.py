S = int(input())

dp = [21e8] * (S * 2 + 1)
dp[1] = 0

for i in range(1, S * 2 + 1):
    # 지금 있는 걸 복사해서 붙여넣기
    cnt = dp[i] + 1 # 복사
    for j in range(i + i, S * 2 + 1, i):
        cnt += 1 # 붙여넣기
        dp[j] = min(dp[j], cnt)

        dp[j - 1] = min(dp[j - 1], dp[j] + 1)

print(dp[S])