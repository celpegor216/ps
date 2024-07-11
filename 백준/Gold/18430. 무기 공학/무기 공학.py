N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

left = [(0, 1), (1, 0), (0, -1), (-1, 0)]
right = [(1, 0), (0, -1), (-1, 0), (0, 1)]

used = [[0] * M for _ in range(N)]
result = 0

def dfs(y, x, total):
    global result

    result = max(result, total)

    if y == N:
        return
    
    if not used[y][x]:
        for i in range(4):
            ly, lx, ry, rx = y + left[i][0], x + left[i][1], y + right[i][0], x + right[i][1]
            if 0 <= ly < N and 0 <= lx < M and not used[ly][lx] and 0 <= ry < N and 0 <= rx < M and not used[ry][rx]:
                used[ly][lx] = 1
                used[ry][rx] = 1
                used[y][x] = 1

                if x + 1 == M:
                    dfs(y + 1, 0, total + lst[y][x] * 2 + lst[ly][lx] + lst[ry][rx])
                else:
                    dfs(y, x + 1, total + lst[y][x] * 2 + lst[ly][lx] + lst[ry][rx])

                used[y][x] = 0
                used[ly][lx] = 0
                used[ry][rx] = 0

    if x + 1 == M:
        dfs(y + 1, 0, total)
    else:
        dfs(y, x + 1, total)

dfs(0, 0, 0)

print(result)