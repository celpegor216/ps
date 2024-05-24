# dp 같은데 해결 방법을 모르겠음
# 해답: https://wooono.tistory.com/605

N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]

# 0번째 행은 왼>오만 가능
for m in range(1, M):
    dp[0][m] += dp[0][m - 1]

# 1번째 행부터는 왼>오, 위>아래, 오>왼 가능
for n in range(1, N):
    ltr = dp[n][:]
    rtl = dp[n][:]

    # 왼>오와 위>아래 비교
    for m in range(M):
        if m == 0:
            ltr[m] += dp[n - 1][m]
        else:
            ltr[m] += max(dp[n - 1][m], ltr[m - 1])

    # 오>왼과 위>아래 비교
    for m in range(M - 1, -1, -1):
        if m == M - 1:
            rtl[m] += dp[n - 1][m]
        else:
            rtl[m] += max(dp[n - 1][m], rtl[m + 1])

    for m in range(M):
        dp[n][m] = max(ltr[m], rtl[m])

print(dp[-1][-1])