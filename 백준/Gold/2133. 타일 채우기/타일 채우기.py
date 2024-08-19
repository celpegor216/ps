N = int(input())

if N % 2:
    print(0)
elif N == 2:
    print(3)
elif N == 4:
    print(11)
else:
    dp = [0] * (N // 2)
    dp[0] = 3
    dp[1] = 11

    for n in range(2, N // 2):
        dp[n] = dp[n - 1] * 3 + 2
        for m in range(n - 1):
            dp[n] += dp[m] * 2

    print(dp[-1])