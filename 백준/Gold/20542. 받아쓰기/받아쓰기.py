# 힌트: dp (1 ≤ n × m ≤ 10,000,000)
# 해답: https://ddiyeon.tistory.com/69
# 편집거리 알고리즘 + 제약 조건(v=v,w / i=i,j,l)

N, M = map(int, input().split())
A = ' ' + input() # 답안
B = ' ' + input() # 정답

dp = [[0] * (M + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    dp[n][0] = n

for m in range(1, M + 1):
    dp[0][m] = m

for n in range(1, N + 1):
    for m in range(1, M + 1):
        # 비교 문자가 다른 경우
        dp[n][m] = min(dp[n][m - 1], dp[n - 1][m], dp[n - 1][m - 1]) + 1

        # 비교 문자가 같은 경우
        if A[n] == B[m] or (A[n] == 'v' and B[m] == 'w') or (A[n] == 'i' and B[m] in 'jl'):
            dp[n][m] = dp[n - 1][m - 1]

print(dp[-1][-1])