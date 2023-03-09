# 해답 듣고 DP로 풀기

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for n in range(N - 1, -1, -1):
    if n + lst[n][0] <= N:
        dp[n] = lst[n][1] + max(dp[n + lst[n][0]:])
    
print(max(dp))