# dp 같은데 규칙을 못 찾겠음
# 해답: https://orchemi.github.io/boj%20gold%20iv/BOJ_TD01_14852/

N = int(input())
mod = 1000000007

dp = [0, 2, 7]

if N < 3:
    print(dp[N])
else:
    b3, b2, b1 = dp

    cnt = 2
    befores = 1

    while cnt < N:
        # dp[cnt - 1] * 2 + dp[cnt - 2] * 3
        # + (dp[cnt - 3] + dp[cnt -4] + ... + dp[1]) * 2
        now = (b1 * 2 + b2 * 3 + befores * 2) % mod
        b3, b2, b1 = b2, b1, now
        cnt += 1
        befores += b3
        befores %= mod
    
    print(b1)