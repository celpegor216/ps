N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

up = [[0] * M for _ in range(N)]

for n in range(N - 1, -1, -1):
    for m in range(M):
        if n == N - 1 and m == 0:
            up[n][m] = lst[n][m]
        elif n == N - 1:
            up[n][m] = up[n][m - 1] + lst[n][m]
        elif m == 0:
            up[n][m] = up[n + 1][m] + lst[n][m]
        else:
            up[n][m] = max(up[n][m - 1] + lst[n][m], up[n + 1][m] + lst[n][m])

down = [[0] * M for _ in range(N)]

for n in range(N - 1, -1, -1):
    for m in range(M - 1, -1, -1):
        if n == N - 1 and m == M - 1:
            down[n][m] = lst[n][m]
        elif n == N - 1:
            down[n][m] = down[n][m + 1] + lst[n][m]
        elif m == M - 1:
            down[n][m] = down[n + 1][m] + lst[n][m]
        else:
            down[n][m] = max(down[n][m + 1] + lst[n][m], down[n + 1][m] + lst[n][m])

result = -21e8

for n in range(N):
    for m in range(M):
        result = max(result, up[n][m] + down[n][m])

print(result)