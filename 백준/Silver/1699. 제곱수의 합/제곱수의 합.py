N = int(input())

dp = [0, 1]

for n in range(2, N + 1):
    half = int(n ** 0.5)
    
    if half == n ** 0.5:
        dp.append(1)
    else:
        temp = []
        
        for i in range(1, half + 1):    
            temp.append(dp[i ** 2] + dp[n - i ** 2])
        
        dp.append(min(temp))

print(dp[-1])