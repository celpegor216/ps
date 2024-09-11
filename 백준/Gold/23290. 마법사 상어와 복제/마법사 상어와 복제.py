#  4 × 4 크기의 격자
N = 4
# 이동 방향은 8가지 방향(상하좌우, 대각선) 중 하나
D = 8
# 물고기 M마리, 연습 횟수 S
M, S = map(int, input().split())
# 물고기의 위치 y, x, 이동 방향 d
# 둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.
# lst[i][j][k]: i, j 위치에서 k번 방향을 향하고 있는 물고기의 수
lst = [[[0] * D for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    y, x, d = map(int, input().split())
    lst[y][x][d - 1] += 1

# 방향은 8 이하의 자연수로 표현하고, 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
directions = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
# 상은 1, 좌는 2, 하는 3, 우는 4로 변환
shark_directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

# 상어도 격자의 한 칸에 들어가있다
sy, sx = map(int, input().split())

# smells[i][j][k]: i, j 위치에 k + 1 번 전 연습에서 생긴 물고기의 냄새
K = 2
smells = [[[0] * K for _ in range(N + 1)] for _ in range(N + 1)]

# S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수를 구해보자.
for _ in range(S):
    # 상어가 모든 물고기에게 복제 마법을 시전한다
    # 복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.
    copied = [[[0] * D for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for d in range(D):
                copied[i][j][d] = lst[i][j][d]

    # 모든 물고기가 한 칸 이동한다.
    # 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.
    # 그 외의 경우에는 그 칸으로 이동을 한다.
    new_lst = [[[0] * D for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if not sum(lst[i][j]):
                continue

            cannot_move = []

            for d in range(D - 1, -D - 1, -1):
                dy, dx = directions[d]
                ny, nx = i + dy, j + dx
                # 상어가 있는 칸, 물고기의 냄새가 있는 칸,
                # 격자의 범위를 벗어나는 칸으로는 이동할 수 없다.
                if not (0 < ny <= N and 0 < nx <= N) or (ny == sy and nx == sx) or sum(smells[ny][nx]):
                    # 각 물고기는 자신이 가지고 있는 이동 방향이
                    # 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
                    if lst[i][j][d]:
                        cannot_move.append((d, lst[i][j][d]))
                        lst[i][j][d] = 0
                else:
                    cannot_move.append((d, lst[i][j][d]))
                    lst[i][j][d] = 0
                    for dd, v in cannot_move:
                        new_lst[ny][nx][d] += v
                    cannot_move = []

            for d, v in cannot_move:
                new_lst[i][j][d] += v

    lst = new_lst

    # 상어 이동
    # 상어가 연속해서 3칸 이동한다.
    # 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다.
    # 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며,
    # 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다.
        # 먼저, 방향을 정수로 변환해야 한다. 상은 1, 좌는 2, 하는 3, 우는 4로 변환
        # 변환을 모두 마쳤으면, 수를 이어 붙여 정수로 하나 만든다
        # a < b를 만족하면 A가 B보다 사전 순으로 앞선 것
    ry, rx = sy, sx
    max_fish_path = []    # 제외되는 물고기들의 좌표
    max_fish_cnt = -1    # 제외되는 물고기 수
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ny, nx = sy, sx
                fish_path = []
                fish_cnt = 0
                for d in (i, j, k):
                    ny += shark_directions[d][0]
                    nx += shark_directions[d][1]
                    # 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능
                    if not (0 < ny <= N and 0 < nx <= N):
                        break

                    if (ny, nx) not in fish_path and sum(lst[ny][nx]):
                        fish_path.append((ny, nx))
                        fish_cnt += sum(lst[ny][nx])
                else:
                    if max_fish_cnt < fish_cnt:
                        ry, rx = ny, nx
                        max_fish_path = fish_path
                        max_fish_cnt = fish_cnt

    sy, sx = ry, rx


    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
            smells[i][j][1] = smells[i][j][0]
            smells[i][j][0] = 0

            # 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면,
            # 그 칸에 있는 모든 물고기는 격자에서 제외되며,
            # 제외되는 모든 물고기는 물고기 냄새를 남긴다.
            if (i, j) in max_fish_path:
                lst[i][j] = [0] * D
                smells[i][j][0] = 1

            # 1에서 사용한 복제 마법이 완료된다.
            # 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
            for d in range(D):
                lst[i][j][d] += copied[i][j][d]

result = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        result += sum(lst[i][j])

print(result)
