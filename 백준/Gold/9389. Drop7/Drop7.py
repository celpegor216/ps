N = 7


def check(board):
    while 1:
        flag = 0
        removed = [[0] * N for _ in range(N)]

        # 열 체크
        for j in range(N):
            cnt = 0
            for i in range(N):
                if board[i][j]:
                    cnt += 1

            if not cnt:
                continue

            for i in range(N):
                if board[i][j] == cnt:
                    removed[i][j] = 1
                    flag = 1

        # 행 체크
        for i in range(N):
            cnt = 0
            start = -1

            for j in range(N):
                if board[i][j]:
                    cnt += 1
                    if start == -1:
                        start = j
                else:
                    for k in range(cnt):
                        if board[i][start + k] == cnt:
                            removed[i][start + k] = 1
                            flag = 1
                    cnt = 0
                    start = -1

            if cnt:
                for k in range(cnt):
                    if board[i][start + k] == cnt:
                        removed[i][start + k] = 1
                        flag = 1


        # 하나도 안 터진 경우
        if not flag:
            break


        # 중력 적용
        new_board = [[0] * N for _ in range(N)]
        for j in range(N):
            idx = N - 1
            for i in range(N - 1, -1, -1):
                if not removed[i][j] and board[i][j]:
                    new_board[idx][j] = board[i][j]
                    idx -= 1

        board = new_board

    return board


def play(K):
    board = [[0] * N for _ in range(N)]
    cmds = [list(map(int, input().split())) for _ in range(K)]

    for v, x in cmds:
        x -= 1

        # 떨어뜨리기
        y = -1
        while y < N - 1:
            if board[y + 1][x]:
                break
            y += 1

        if y == -1:
            return 'Game Over!\n'

        board[y][x] = v

        board = check(board)

    result = ''
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                result += '#'
            else:
                result += str(board[i][j])
        result += '\n'

    return result


while 1:
    K = int(input())

    if not K:
        break

    print(play(K))