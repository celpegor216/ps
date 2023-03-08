N = int(input())
P = list(map(int, input().split()))

dp = [P[0]]

for n in range(1, N):
    temp = [P[n]]
    
    for i in range(n):
        temp.append(dp[n - i - 1] + P[i])
    
    dp.append(min(temp))

print(dp[-1])