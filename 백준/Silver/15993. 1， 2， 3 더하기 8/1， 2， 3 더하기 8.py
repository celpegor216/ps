dp = [[0] * 2 for _ in range(100001)]    # 사용한 수의 개수가 홀수, 짝수
dp[1][0] = 1
dp[2][0] = 1
dp[3][0] = 1

for n in range(2, 100001):
    dp[n][0] += (dp [n - 3][1] + dp[n - 2][1] + dp[n - 1][1]) % 1000000009
    dp[n][1] += (dp [n - 3][0] + dp[n - 2][0] + dp[n - 1][0]) % 1000000009

T = int(input())

for _ in range(T):
    print(*dp[int(input())])