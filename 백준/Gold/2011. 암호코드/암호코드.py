S = input()

if S[0] == '0' or '00' in S:
    print(0)
else:
    N = len(S)

    dp = [0] * (N + 1)
    dp[0] = dp[1] = 1

    for i in range(2, N + 1):
        if S[i - 1] != '0':
            dp[i] += dp[i - 1]
        if 10 <= int(S[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    print(dp[-1] % (10 ** 6))