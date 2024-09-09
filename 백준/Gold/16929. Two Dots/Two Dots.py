N, M = map(int, input().split())
lst = [input() for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
# used[i][j][d]: d로 이동해서 (i, j)에 온 적이 있는지 여부
used = [[[0] * 4 for _ in range(M)] for _ in range(N)]

result = 0
def dfs(y, x):
    global result

    if sum(used[y][x]):
        result = 1
        return

    for d in range(4):
        if used[y][x][d]:
            continue

        dy, dx = directions[d]
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < M and not used[ny][nx][(d + 2) % 4] and lst[ny][nx] == lst[y][x]:
            used[y][x][d] = 1
            dfs(ny, nx)
            used[y][x][d] = 0

        if result:
            return


def find():
    for i in range(N):
        for j in range(M):
            dfs(i, j)

            if result:
                return

find()

print('Yes' if result else 'No')