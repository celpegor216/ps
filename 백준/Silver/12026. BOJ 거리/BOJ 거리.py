# 힌트: dp
# 해답: https://devlibrary00108.tistory.com/123

N = int(input())
S = input()
dp = [21e8] * N
dp[0] = 0

for i in range(1, N):
    for j in range(i):
        if (S[j] == 'B' and S[i] == 'O') or (S[j] == 'O' and S[i] == 'J') or (S[j] == 'J' and S[i] == 'B'):
            dp[i] = min(dp[i], dp[j] + (i - j) ** 2)

if dp[-1] == 21e8:
    print(-1)
else:
    print(dp[-1])