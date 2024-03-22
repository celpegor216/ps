N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

iy = ix = -1

for n in range(N):
    for m in range(M):
        if board[n][m] == 'I':
            iy = n
            ix = m
            break

command = input()

dy = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

cnt = 0
flag = 0

for c in command:
    # 1. 종수 아두이노 이동
    c = int(c)

    iy += dy[c]
    ix += dx[c]

    cnt += 1

    # 2. 종수 아두이노가 미친 아두이노 만나면 게임에서 지고 끝
    if board[iy][ix] == 'R':
        flag = 1
        break

    # 3. 미친 아두이노들이 이동
    tmp_board = [[0] * M for _ in range(N)]

    for n in range(N):
        for m in range(M):
            if board[n][m] == 'R':
                minv = 21e8
                mind = 0

                for d in range(1, 10):
                    nn, nm = n + dy[d], m + dx[d]

                    if 0 <= nn < N and 0 <= nm < M:
                        tmp = abs(nn - iy) + abs(nm - ix)
                        if tmp < minv:
                            minv = tmp
                            mind = d
                
                tmp_board[n + dy[mind]][m + dx[mind]] += 1
    
    # 4. 미친 아두이노가 종수 아두이노 만나면 게임에서 지고 끝
    if tmp_board[iy][ix]:
        flag = 1
        break

    # 5. 2개 이상의 미친 아두이노가 같은 칸에 있으면 폭발
    for n in range(N):
        for m in range(M):
            if tmp_board[n][m] == 1:
                board[n][m] = 'R'
            else:
                board[n][m] = '.'

    board[iy][ix] = 'I'

if flag:
    print(f'kraj {cnt}')
else:
    for line in board:
        print(''.join(line))