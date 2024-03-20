board = [[] for _ in range(4)]

for i in range(4):
    tmp = list(map(int, input().split()))

    for j in range(4):
        board[i].append([tmp[j * 2], tmp[j * 2 + 1]])

ds = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

result = 0

def fish_move(sy, sx, num, next_board):
    for i in range(4):
        for j in range(4):
            if next_board[i][j] and next_board[i][j][0] == num:
                d = next_board[i][j][1]
                for _ in range(8):
                    ny, nx = i + ds[d][0], j + ds[d][1]
                    if 0 <= ny < 4 and 0 <= nx < 4 and not (ny == sy and nx == sx):
                        next_board[i][j] = next_board[ny][nx]
                        next_board[ny][nx] = [num, d]
                        return
                    
                    d += 1
                    if d == 9:
                        d = 1

def shark_move(sy, sx, sd, total, now_board):
    global result

    result = max(result, total)

    next_board = [now_board[i][:] for i in range(4)]

    # 번호가 작은 물고기부터 이동
    for num in range(1, 17):
        fish_move(sy, sx, num, next_board)
    
    # 상어 이동
    for i in range(1, 4):
        ny, nx = sy + ds[sd][0] * i, sx + ds[sd][1] * i

        if not (0 <= ny < 4 and 0 <= nx < 4):
            break

        if next_board[ny][nx]:
            t, d = next_board[ny][nx]
            next_board[ny][nx] = []
            shark_move(ny, nx, d, total + t, next_board)
            next_board[ny][nx] = [t, d]


total, sd = board[0][0]
board[0][0] = []

shark_move(0, 0, sd, total, board)

print(result)