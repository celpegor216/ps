T = int(input())

dp = [[0] * 65 for _ in range(10)]

for i in range(10):
    dp[i][1] = 1

for j in range(2, 65):
    for i in range(10):
        for k in range(i, 10):
            dp[i][j] += dp[k][j - 1]

for _ in range(T):
    N = int(input())

    result = 0
    for i in range(10):
        result += dp[i][N]
    
    print(result)