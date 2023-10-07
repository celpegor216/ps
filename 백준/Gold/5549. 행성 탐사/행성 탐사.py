import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
lst = [input() for _ in range(N)]

dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]

for n in range(N):
    for m in range(M):
        for i in range(3):
            if n > 0:
                dp[n][m][i] += dp[n - 1][m][i]
            if m > 0:
                dp[n][m][i] += dp[n][m - 1][i]
            if n > 0 and m > 0:
                dp[n][m][i] -= dp[n - 1][m - 1][i]
        
        if lst[n][m] == 'J':
            dp[n][m][0] += 1
        elif lst[n][m] == 'O':
            dp[n][m][1] += 1
        else:
            dp[n][m][2] += 1

for _ in range(K):
    sy, sx, ey, ex = map(int, input().split())
    sy -= 1
    sx -= 1
    ey -= 1
    ex -= 1

    for i in range(3):
        temp = dp[ey][ex][i]
        
        if sy > 0:
            temp -= dp[sy - 1][ex][i]
        if sx > 0:
            temp -= dp[ey][sx - 1][i]
        if sy > 0 and sx > 0:
            temp += dp[sy - 1][sx - 1][i]

        print(temp, end=' ')
    print()