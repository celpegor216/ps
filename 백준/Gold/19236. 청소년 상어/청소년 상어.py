# 4×4크기
N = 4
K = N ** 2
# 한 칸에는 물고기가 한 마리, 각 물고기는 번호와 방향
# 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며,
# 두 물고기가 같은 번호를 갖는 경우는 없다
# ai는 물고기의 번호, bi는 방향
fish = [[] for _ in range(K + 1)]
lst = []
for i in range(N):
    tmp = list(map(int, input().split()))
    line = []

    for j in range(N):
        a, b = tmp[j * 2], tmp[j * 2 + 1]
        fish[a] = [i, j, b - 1]
        line.append(a)

    lst.append(line)


# 방향은 8가지 방향, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗
D = 8
directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

# 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다.
start_d = fish[lst[0][0]][-1]
start_total = lst[0][0]
fish[lst[0][0]] = []
lst[0][0] = -1

result = start_total
def dfs(now_lst, now_fish, sy, sx, sd, total):
    global result

    result = max(result, total)

    # 물고기가 번호가 작은 물고기부터 순서대로 이동
    moved_lst = [line[:] for line in now_lst]
    moved_fish = [line[:] for line in now_fish]

    for k in range(1, K + 1):
        # 이미 잡아먹힌 물고기는 건너뛰기
        if not moved_fish[k]:
            continue

        y, x, d = moved_fish[k]

        # 물고기는 한 칸을 이동할 수 있고,
        # 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
        # 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다
        for _ in range(D):
            dy, dx = directions[d]
            ny, nx = y + dy, x + dx

            # 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸
            if not (0 <= ny < N and 0 <= nx < N) or moved_lst[ny][nx] == -1:
                d = (d + 1) % D
                continue

            # 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
            if not moved_lst[ny][nx]:
                moved_lst[y][x], moved_lst[ny][nx] = moved_lst[ny][nx], moved_lst[y][x]
                moved_fish[k] = [ny, nx, d]
            else:
            # 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식
                oppo = moved_lst[ny][nx]
                moved_lst[y][x], moved_lst[ny][nx] = moved_lst[ny][nx], moved_lst[y][x]
                moved_fish[k] = [ny, nx, d]
                moved_fish[oppo][0] = y
                moved_fish[oppo][1] = x
            break


    # 물고기의 이동이 모두 끝나면 상어가 이동
    # 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
    # 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
    dy, dx = directions[sd]
    ny, nx = sy, sx
    for _ in range(N):
        ny += dy
        nx += dx

        if not(0 <= ny < N and 0 <= nx < N):
            break

        # 물고기가 없는 칸으로는 이동할 수 없다.
        if not moved_lst[ny][nx]:
            continue

        # 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고,
        # 그 물고기의 방향을 가지게 된다.
        nxt_lst = [line[:] for line in moved_lst]
        nxt_fish = [line[:] for line in moved_fish]
        nxt_total = total

        f = nxt_lst[ny][nx]
        nxt_total += f
        nxt_lst[sy][sx] = 0
        nxt_lst[ny][nx] = -1
        nd = nxt_fish[f][-1]
        nxt_fish[f] = []

        dfs(nxt_lst, nxt_fish, ny, nx, nd, nxt_total)


dfs(lst, fish, 0, 0, start_d, start_total)

# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값
print(result)