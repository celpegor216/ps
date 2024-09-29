N, M = map(int, input().split())

# 벽이 있는 칸은 #, 빈칸은 ., 탐정의 위치는 D, 도둑의 위치는 R
lst = [input() for _ in range(N)]

sy = sx = ey = ex = -1

# 보드의 테두리, 즉 1행, 1열, N행, M열에 해당하는 칸은 벽
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if lst[i][j] == 'D':
            sy, sx = i, j
        elif lst[i][j] == 'R':
            ey, ex = i, j


directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
move_blanks = [
    # top, up, right, down, left, bottom
    [2, 1, 5, 3, 0, 4],
    [4, 1, 0, 3, 5, 2],
    [3, 0, 2, 5, 4, 1],
    [1, 5, 2, 0, 4, 3],
]


# 감옥을 최소 몇 번 굴려야 당신이 게임에서 승리할 수 있을지 알아보자 > bfs
# used 배열을 어떻게 만들 것인지가 관건
def find():
    # used[i][j][k]: 주사위의 뚫려있는 면이 k에 있을 때 해당 칸에 도착 여부
    # k는 0부터 5까지 top, up, right, down, left, bottom
    used = [[[0] * 6 for _ in range(M)] for _ in range(N)]

    # 탐정은 자신이 있는 칸에 감옥의 뚫린 면이 바닥을 향하게 하여 놓는다
    blank = 5

    used[sy][sx][blank] = 1

    q = [(sy, sx, blank)]
    result = 0
    while q:
        nq = []

        for y, x, blank in q:
            if y == ey and x == ex:
                if blank == 5:
                    return result
                else:
                    continue

            for i in range(4):
                dy, dx = directions[i]
                ny, nx = y + dy, x + dx
                if lst[ny][nx] == '#':
                    continue

                nxt_blank = move_blanks[i][blank]
                
                if used[ny][nx][nxt_blank]:
                    continue
                
                used[ny][nx][nxt_blank] = 1
                nq.append((ny, nx, nxt_blank))

        q = nq
        result += 1
    
    return -1


print(find())