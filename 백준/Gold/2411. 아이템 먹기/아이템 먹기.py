N, M, A, B = map(int, input().split())

transform = lambda x: int(x) - 1

items = []
for _ in range(A):
    y, x = map(transform, input().split())
    items.append((N - 1 - y, x))

lst = [[0] * M for _ in range(N)]
for _ in range(B):
    y, x = map(transform, input().split())
    lst[N - 1 - y][x] = 1

dp = [[0] * M for _ in range(N)]
dp[-1][0] = 1

items.append((N - 1, 0))
items.append((0, M - 1))
items.sort(key=lambda x: (-x[0], x[1]))


for i in range(len(items) - 1):
    sy, sx = items[i]
    ey, ex = items[i + 1]

    for a in range(sy, ey - 1, -1):
        for b in range(sx, ex + 1):
            if lst[a][b] or (a == sy and b == sx):
                continue

            if a < N - 1:
                dp[a][b] += dp[a + 1][b]
            if b > 0:
                dp[a][b] += dp[a][b - 1]

print(dp[0][-1])