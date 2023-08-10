# 힌트: dp
# 해답: https://velog.io/@cgw0519/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EB%B0%B1%EC%A4%80-10653-%EB%A7%88%EB%9D%BC%ED%86%A4-2

N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[21e8] * N for _ in range(K + 1)]

for k in range(K + 1):
    for n in range(N):
        if n == 0:
            dp[k][n] = 0
        else:
            if k == 0:
                dp[k][n] = dp[k][n - 1] + abs(lst[n][0] - lst[n - 1][0]) + abs(lst[n][1] - lst[n - 1][1])
            else:
                if n == 1:
                    dp[k][n] = dp[k - 1][n]
                else:
                    dp[k][n] = dp[0][n]
                    dp[k][n] = min([dp[k - i][n - i - 1] + abs(lst[n][0] - lst[n - i - 1][0]) + abs(lst[n][1] - lst[n - i - 1][1]) for i in range(k + 1)])

print(min([dp[x][-1] for x in range(K + 1)]))