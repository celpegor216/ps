N = 9


def pos_to_idx(pos):
    return ord(pos[0]) - ord('A'), int(pos[1]) - 1


def fill(y, x, a):
    lst[y][x] = a
    rows[y][a] = 1
    cols[x][a] = 1
    boxes[(y // 3) * 3 + x // 3][a] = 1


def remove(y, x, a):
    lst[y][x] = -1
    rows[y][a] = 0
    cols[x][a] = 0
    boxes[(y // 3) * 3 + x // 3][a] = 0


def check(y, x, a):
    return rows[y][a] or cols[x][a] or boxes[(y // 3) * 3 + x // 3][a]


def dfs(y, x):
    global result

    if result:
        return

    if y == N:
        result = [line[:] for line in lst]
        return

    ny, nx = y, x
    nx += 1
    if nx == N:
        nx = 0
        ny += 1

    # 이미 차있는 경우
    if lst[y][x] != -1:
        dfs(ny, nx)
    else:
        # 지금 위치에서 오른쪽으로 채울 수 있는지 확인
        if x + 1 < N and lst[y][x + 1] == -1:
            # 아직 사용하지 않은 타일 중에서 채울 수 있는 게 있는지 확인
            for i in range(N):
                for j in range(N):
                    if i == j or dominos[i][j]:
                        continue

                    if check(y, x, i) or check(y, x + 1, j):
                        continue

                    dominos[i][j] = 1
                    dominos[j][i] = 1
                    fill(y, x, i)
                    fill(y, x+ 1, j)

                    dfs(ny, nx)

                    dominos[i][j] = 0
                    dominos[j][i] = 0
                    remove(y, x, i)
                    remove(y, x+ 1, j)

        # 지금 위치에서 아래쪽으로 채울 수 있는지 확인
        if y + 1 < N and lst[y + 1][x] == -1:
            # 아직 사용하지 않은 타일 중에서 채울 수 있는 게 있는지 확인
            for i in range(N):
                for j in range(N):
                    if i == j or dominos[i][j]:
                        continue

                    if check(y, x, i) or check(y + 1, x, j):
                        continue

                    dominos[i][j] = 1
                    dominos[j][i] = 1
                    fill(y, x, i)
                    fill(y + 1, x, j)

                    dfs(ny, nx)

                    dominos[i][j] = 0
                    dominos[j][i] = 0
                    remove(y, x, i)
                    remove(y + 1, x, j)


tc = 0
while 1:
    tc += 1

    K = int(input())

    if K == 0:
        break

    lst = [[-1] * N for _ in range(N)]
    # dominos[i][j]: i-j가 연결된 도미노의 사용 여부
    dominos = [[0] * N for _ in range(N)]

    rows = [[0] * N for _ in range(N)]
    cols = [[0] * N for _ in range(N)]
    boxes = [[0] * N for _ in range(N)]

    for _ in range(K):
        U, LU, V, LV = input().split()
        U, V = int(U) - 1, int(V) - 1
        fill(*pos_to_idx(LU), U)
        fill(*pos_to_idx(LV), V)
        dominos[U][V] = 1
        dominos[V][U] = 1

    positions = input().split()
    for n in range(N):
        fill(*pos_to_idx(positions[n]), n)

    result = []
    dfs(0, 0)

    print(f'Puzzle {tc}')
    for line in result:
        for item in line:
            print(item + 1, end='')
        print()