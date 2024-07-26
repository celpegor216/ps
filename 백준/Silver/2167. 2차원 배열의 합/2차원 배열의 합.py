N, M = map(int, input().split())
lst = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

memo = [[0] * (M + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    for m in range(1, M + 1):
        memo[n][m] = memo[n - 1][m] + memo[n][m - 1] - memo[n - 1][m - 1] + lst[n][m]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i - 1][y] - memo[x][j - 1] + memo[i - 1][j - 1])