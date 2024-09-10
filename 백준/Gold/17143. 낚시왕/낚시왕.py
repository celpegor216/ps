# 격자판의 크기 R, C와 상어의 수 M
# r은 행, c는 열이고, (R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸
N, M, K = map(int, input().split())
# 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.
lst = [[[] for _ in range(M)] for _ in range(N)]
# 위치 y, x, 속력 s, 이동 방향 d, 크기 z
for k in range(K):
    y, x, s, d, z = map(int, input().split())
    lst[y - 1][x - 1].append((s, d - 1, z, chr(ord('A') + k)))

# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
directions_oppo = (1, 0, 3, 2)


# 낚시왕이 잡은 상어 크기의 합
result = 0
# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다.
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.
for m in range(M):
    # 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다
    # 낚시왕이 오른쪽으로 한 칸 이동한다.

    # 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for n in range(N):
        if lst[n][m]:
            result += lst[n][m].pop()[2]
            break

    # 상어가 이동한다.
    # 상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초
    # 상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동
    new_lst = [[[] for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not lst[i][j]:
                continue

            s, d, z, c = lst[i][j].pop()
            ny, nx = i, j

            if s:
                dy, dx = directions[d]
                # 상하 이동에서 초과 칸이 발생한 경우
                if not(0 <= ny + dy * s < N):
                    left = s - ny if d == 0 else s - (N - 1 - ny)
                    cycle = (N - 1) * 2
                    left %= cycle
                    if not left:
                        left = cycle
                    d = directions_oppo[d]
                    if left > N - 1:
                        d = directions_oppo[d]
                        left -= (N - 1)
                    ny = N - 1 - left if d == 0 else left

                # 좌우 이동에서 초과 칸이 발생한 경우
                elif not(0 <= nx + dx * s < M):
                    left = s - nx if d == 3 else s - (M - 1 - nx)
                    cycle = (M - 1) * 2
                    left %= cycle
                    if not left:
                        left = cycle
                    d = directions_oppo[d]
                    if left > M - 1:
                        d = directions_oppo[d]
                        left -= (M - 1)
                    nx = M - 1 - left if d == 3 else left

                # 초과 칸이 발생하지 않은 경우
                else:
                    ny += dy * s
                    nx += dx * s

            # 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다.
            # 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
            if not new_lst[ny][nx] or new_lst[ny][nx][0][2] < z:
                new_lst[ny][nx] = [(s, d, z, c)]

    lst = new_lst


print(result)