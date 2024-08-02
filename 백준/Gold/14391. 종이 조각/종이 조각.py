N, M = map(int, input().split())
lst = [list(map(int, input())) for _ in range(N)]

memo_horizontal = [[[0] * M for _ in range(M)] for _ in range(N)]
memo_vertical = [[[0] * N for _ in range(N)] for _ in range(M)]

for i in range(N):
    for j in range(M):
        for k in range(j, M):
            memo_horizontal[i][j][k] = memo_horizontal[i][j][k - 1] * 10 + lst[i][k]

for i in range(M):
    for j in range(N):
        for k in range(j, N):
            memo_vertical[i][j][k] = memo_vertical[i][j][k - 1] * 10 + lst[k][i]

def dfs(sy, sx, ey, ex):
    if sy == ey and sx == ex:
        return lst[sy][sx]

    if sy == ey:
        tmp = [memo_horizontal[sy][sx][ex]]
        for i in range(sx, ex):
            tmp.append(dfs(sy, sx, ey, i) + dfs(sy, i + 1, ey, ex))
        return max(tmp)

    if sx == ex:
        tmp = [memo_vertical[sx][sy][ey]]
        for i in range(sy, ey):
            tmp.append(dfs(sy, sx, i, ex) + dfs(i + 1, sx, ey, ex))
        return max(tmp)

    tmp = []
    for i in range(sy, ey):
        tmp.append(dfs(sy, sx, i, ex) + dfs(i + 1, sx, ey, ex))
    for i in range(sx, ex):
        tmp.append(dfs(sy, sx, ey, i) + dfs(sy, i + 1, ey, ex))

    return max(tmp)

print(dfs(0, 0, N - 1, M - 1))