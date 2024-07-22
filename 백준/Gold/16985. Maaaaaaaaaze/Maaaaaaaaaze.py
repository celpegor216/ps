from collections import deque

boards = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

check = set()

result = 21e8

def bfs(lst):
    global result

    # for line in lst:
    #     print(line)

    q = deque()
    used = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(5)]

    if lst[0][0][0] and lst[4][4][4]:
        q.append((0, 0, 0, 4, 4, 4, 0, 1))
        used[1][0][0][0] = 1
    if lst[0][4][0] and lst[4][0][4]:
        q.append((0, 4, 0, 4, 0, 4, 0, 2))
        used[2][0][4][0] = 1
    if lst[4][0][0] and lst[0][4][4]:
        q.append((4, 0, 0, 0, 4, 4, 0, 3))
        used[3][4][0][0] = 1
    if lst[4][4][0] and lst[0][0][4]:
        q.append((4, 4, 0, 0, 0, 4, 0, 4))
        used[4][4][4][0] = 1

    while q:
        y, x, z, ey, ex, ez, c, t = q.popleft()

        if y == ey and x == ex and z == ez:
            result = min(result, c)
            return

        for dy, dx, dz in ((0, 1, 0), (0, 0, 1), (1, 0, 0), (0, -1, 0), (0, 0, -1), (-1, 0, 0)):
            ny, nx, nz = y + dy, x + dx, z + dz

            if 0 <= ny < 5 and 0 <= nx < 5 and 0 <= nz < 5 and lst[ny][nx][nz] and not used[t][ny][nx][nz]:
                q.append((ny, nx, nz, ey, ex, ez, c + 1, t))
                used[t][ny][nx][nz] = 1

used_boards = [0] * 5

def dfs(level, lst):
    if level == 5:

        c = []
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    c.append(lst[i][j][k])

        c = tuple(c)

        if c not in check:
            check.add(c)
            bfs(lst)
        return

    for k in range(5):
        if not used_boards[k]:
            used_boards[k] = 1

            now_board = [boards[k][n][:] for n in range(5)]

            for n in range(4):
                new_board = []

                for j in range(5):
                    tmp = []
                    for i in range(4, -1, -1):
                        tmp.append(now_board[i][j])
                    new_board.append(tmp)

                tmp_lst = []

                for board in lst:
                    tmp_lst.append([board[n][:] for n in range(5)])

                tmp_lst.append(new_board)
                dfs(level + 1, tmp_lst)

                now_board = new_board

            used_boards[k] = 0

dfs(0, [])

print(result if result != 21e8 else -1)