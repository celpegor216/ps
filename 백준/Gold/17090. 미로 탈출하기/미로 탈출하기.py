import sys
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

used = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]

d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def func(y, x):
    if not used[y][x]:
        used[y][x] = 1

        ny, nx = y + d[lst[y][x]][0], x + d[lst[y][x]][1]

        if not (0 <= ny < N and 0 <= nx < M):
            dp[y][x] = 1
        else:
            dp[y][x] = func(ny, nx)

    return dp[y][x]

result = 0

for n in range(N):
    for m in range(M):
        if not used[n][m]:
            func(n, m)

for line in dp:
    result += sum(line)

print(result)