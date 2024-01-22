# dp 같은데 쿠폰을 어떻게 해야 할 지 모르겠음
# 해답: https://black-hair.tistory.com/111

N, M = map(int, input().split())
visit = [1] * (110)

if M:
    tmp = list(map(int, input().split()))
    for item in tmp:
        visit[item] = 0

coupon = 0
dp = [[21e8 for _ in range(110)] for _ in range(110)]    # N번째 날에 M개의 쿠폰을 가지고 있는 경우
dp[0][0] = 0

for i in range(N + 1):
    for j in range(40):    # 생길 수 있는 최대 쿠폰 수 40
        if dp[i][j] == 21e8:
            continue

        result = dp[i][j]

        # 리조트에 못 가는 경우
        if not visit[i + 1]:
            dp[i + 1][j] = min(result, dp[i + 1][j])

        # 쿠폰을 사용할 수 있는 경우
        if j >= 3:
            dp[i + 1][j - 3] = min(result, dp[i + 1][j - 3])
        
        # 1일권 구매
        dp[i + 1][j] = min(result + 10000, dp[i + 1][j])

        # 3일권 구매
        for k in range(1, 4):
            dp[i + k][j + 1] = min(result + 25000, dp[i + k][j + 1])
        
        # 5일권 구매
        for k in range(1, 6):
            dp[i + k][j + 2] = min(result + 37000, dp[i + k][j + 2])

print(min(dp[N]))