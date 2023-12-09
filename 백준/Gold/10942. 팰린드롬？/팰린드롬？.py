import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

dp = [[1] * N for _ in range(N)]

for n in range(N - 1, -1, -1):
    for m in range(n, N):
        if dp[n][m]:
            if lst[n] != lst[m]:
                dn, dm = n, m
                while 0 <= dn < N and 0 <= dm < N:
                    dp[dn][dm] = 0
                    dn -= 1
                    dm += 1

M = int(input())

for m in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])