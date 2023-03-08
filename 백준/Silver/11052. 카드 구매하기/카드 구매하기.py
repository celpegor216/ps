N = int(input())
P = list(map(int, input().split()))

dp = [0]

for n in range(1, N + 1):
    temp = []
    
    for i in range(n):
        temp.append(dp[n - i - 1] + P[i])
    
    dp.append(max(temp))

print(dp[-1])