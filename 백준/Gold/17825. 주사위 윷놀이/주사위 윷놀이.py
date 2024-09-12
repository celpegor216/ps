# 시작점 0, 도착점 -1
board = [
    # 분기를 타지 않은 경우
    [0] + [x * 2 for x in range(1, 20)],
    # 10에서 분기를 탄 경우
    [13, 16, 19],
    # 20에서 분기를 탄 경우
    [22, 24],
    # 30에서 분기를 탄 경우
    [28, 27, 26],
    # 25 이후
    [25, 30, 35],
    # 40
    [40]
]

used = [
    [0] * 20,
    [0] * 3,
    [0] * 2,
    [0] * 3,
    [0] * 3,
    [0]
]


# 주사위에서 나올 수 10개를 미리 알고 있을 때, 얻을 수 있는 점수의 최댓값
dice = list(map(int, input().split()))

result = 0
def dfs(level, total, players):
    # players: [[현재 위치한 배열 번호, 배열에서의 인덱스] * 4]
    global result

    # print(level, total, players)

    # 게임은 10개의 턴으로 이루어진다.
    if level == 10 or not players:
        result = max(result, total)
        return

    # 매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴리고,
    # 도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동시킨다.
    length = len(players)
    for i in range(length):
        # 말은 게임판에 그려진 화살표의 방향대로만 이동할 수 있다.
        # 말이 파란색 칸에서 이동을 시작하면 파란색 화살표를 타야 하고,
        # 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를 타야 한다.
        nxt_players = [player[:] for player in players]
        y, x = nxt_players.pop(i)
        now = board[y][x]
        cnt = dice[level]

        used[y][x] = 0

        ny, nx = y, x
        # 10, 20, 30에서 분기를 타는 경우, 한 칸 움직여서 분기에 들어감
        if ny == 0 and now in (10, 20, 30):
            cnt -= 1
            ny, nx = now // 10, 0

        # 10, 20, 30에서 25로 넘어갈 수 있는 경우
        if 0 < ny < 4 and nx + cnt >= len(board[ny]):
            cnt -= (len(board[ny]) - nx)
            ny, nx = 4, 0

        # ny == 0 이거나 25에서 4로 넘어갈 수 있는 경우
        if ny in (0, 4) and nx + cnt >= len(board[ny]):
            cnt -= (len(board[ny]) - nx)
            ny, nx = 5, 0

        nx += cnt

        # 말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다.
        if nx >= len(board[ny]):
            dfs(level + 1, total, nxt_players)
        else:
            # 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다.
            # 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
            if not used[ny][nx]:
                used[ny][nx] = 1
                # 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.
                dfs(level + 1, total + board[ny][nx], nxt_players + [[ny, nx]])
                used[ny][nx] = 0

        used[y][x] = 1


# 처음에는 시작 칸에 말 4개가 있다.
dfs(0, 0, [[0, 0] for _ in range(4)])

print(result)