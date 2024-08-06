N, M = map(int, input().split())

result = 0
used = [[0] * M for _ in range(N)]

def dfs(y, x):
    global result

    if y == N:
        result += 1
        return

    ny = y
    nx = x + 1
    if nx == M:
        nx = 0
        ny += 1

    # 지금 칸을 채우지 않고 넘김
    dfs(ny, nx)

    # 지금 칸이 가장자리이거나,
    # 지금 칸이 오른쪽 아래 칸이라고 생각했을 때 채워도 2 * 2 사각형을 이루지 않는다면
    # 지금 칸을 채우고 넘김
    if (y > 0 and x > 0 and not(used[y - 1][x] and used[y][x - 1] and used[y - 1][x - 1])) or not (y > 0 and x > 0):
        used[y][x] = 1
        dfs(ny, nx)
        used[y][x] = 0

dfs(0, 0)

print(result)