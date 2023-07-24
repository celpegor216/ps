# 힌트: dp
# 해답: https://beginthread.tistory.com/144

N = int(input())
lst = list(map(int, input().split()))

dp = [0] * N

for n in range(1, N):
    temp = 0

    for i in range(n - 1, -1, -1):
        temp = max(temp, dp[i - 1] + max(lst[i:n + 1]) - min(lst[i:n + 1]))
    
    dp[n] = temp

print(dp[-1])