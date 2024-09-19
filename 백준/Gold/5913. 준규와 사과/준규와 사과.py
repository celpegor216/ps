N = 5
K = int(input())
used = [[0] * N for _ in range(N)]
total = N ** 2
for _ in range(K):
    a, b = map(lambda x: int(x) - 1, input().split())
    used[a][b] = 1
    total -= 1

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

result = 0
def dfs(ay, ax, by, bx, cnt):
    global result

    if ay == by and ax == bx:
        if cnt == 0:
            result += 1
        return

    for day, dax in directions:
        nay, nax = ay + day, ax + dax
        if 0 <= nay < N and 0 <= nax < N and not used[nay][nax]:
            for dby, dbx in directions:
                nby, nbx = by + dby, bx + dbx
                if 0 <= nby < N and 0 <= nbx < N and not used[nby][nbx]:
                    used[nay][nax] = 1
                    used[nby][nbx] = 1
                    if nay == nby and nax == nbx:
                        dfs(nay, nax, nby, nbx, cnt - 1)
                    else:
                        dfs(nay, nax, nby, nbx, cnt - 2)
                    used[nby][nbx] = 0
                    used[nay][nax] = 0

used[0][0] = 1
used[-1][-1] = 1
dfs(0, 0, N - 1, N - 1, total - 2)

print(result)