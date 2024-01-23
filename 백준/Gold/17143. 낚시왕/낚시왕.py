# 해답: https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-17143-%EB%82%9A%EC%8B%9C%EC%99%95

R, C, M = map(int, input().split())
board = [[[] for _ in range(C)] for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = list(map(int, input().split()))
    board[r - 1][c - 1] = [s, d, z]

# 위, 아래, 오른쪽, 왼쪽
ds = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]

def move(r, c, s, d):
    if d == 1 or d == 2:
        cycle = R * 2 - 2
        if d == 1:
            s += 2 * (R - 1) - r
        else:
            s += r
        
        s %= cycle
        if s >= R:
            return (cycle - s, c, 1)
        return (s, c, 2)
    else:
        cycle = C * 2 - 2
        if d == 4:
            s += 2 * (C - 1) - c
        else:
            s += c
        
        s %= cycle
        if s >= C:
            return (r, cycle - s, 4)
        return (r, s, 3)

result = 0

for c in range(C):
    idc = -1

    for r in range(R):
        if board[r][c]:
            result += board[r][c][2]
            board[r][c] = []
            break
    
    new_board = [[[] for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c]:
                nr, nc, nd = move(r, c, board[r][c][0], board[r][c][1])
                if new_board[nr][nc]:
                    new_board[nr][nc] = max(new_board[nr][nc], (board[r][c][0], nd, board[r][c][2]), key=lambda x: x[2])
                else:
                    new_board[nr][nc] = (board[r][c][0], nd, board[r][c][2])
    
    board = new_board

print(result)