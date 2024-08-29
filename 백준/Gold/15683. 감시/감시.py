# 사각 지대의 최소 크기를 구하는 프로그램
# CCTV는 벽을 통과할 수 없다, CCTV는 CCTV를 통과할 수 있다
# 6은 벽
# CCTV의 최대 개수는 8개를 넘지 않는다

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

cctv = []
wall = 0
for i in range(N):
    for j in range(M):
        if 0 < lst[i][j] < 6:
            cctv.append((i, j))
        elif lst[i][j] == 6:
            wall += 1
length = len(cctv)

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

used = [[0] * M for _ in range(N)]
result = 0    # 갈 수 있는 넓이의 최댓값
def dfs(level, total):
    global result

    if level == length:
        result = max(result, total)
        return

    # 갈 수 있는 방향 쌍
    i, j = cctv[level]
    for ds in directions[lst[i][j]]:
        # 갈 수 있다고 칠 한 칸들(다시 돌려주기 위함)
        checked = []

        for d in ds:
            dy, dx = dirs[d]
            ny, nx = i, j
            while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != 6:
                if not used[ny][nx]:
                    checked.append((ny, nx))
                    used[ny][nx] = 1
                ny += dy
                nx += dx

        dfs(level + 1, total + len(checked))

        for ny, nx in checked:
            used[ny][nx] = 0

dfs(0, 0)

print(N * M - result - wall)