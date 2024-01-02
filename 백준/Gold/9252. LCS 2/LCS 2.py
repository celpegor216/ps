A = input()
B = input()

a, b = len(A), len(B)

dp = [[0] * (b + 1) for _ in range(a + 1)]

for i in range(1, a + 1):
    for j in range(1, b + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])

if dp[-1][-1]:
    result = ''

    now = dp[-1][-1]

    for i in range(a, 0, -1):
        if now == 0:
            break
        for j in range(b, 0, -1):
            if dp[i][j] == now and A[i - 1] == B[j - 1]:
                result += B[j - 1]
                now -= 1
                break

    print(result[::-1])