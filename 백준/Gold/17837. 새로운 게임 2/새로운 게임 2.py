# 크기가 N×N, 말의 개수는 K
N, K = map(int, input().split())
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나, 0은 흰색, 1은 빨간색, 2는 파란색
board = [list(map(int, input().split())) for _ in range(N)]
# 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다
# 말의 정보는 세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향
# 이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
directions_oppo = (1, 0, 3, 2)

# lst[y][x]: 아래에서부터 위까지 쌓여있는 말의 배열
lst = [[[] for _ in range(N)] for _ in range(N)]
# k번 말의 이동 방향
players_direction = [0] * K
for k in range(K):
    y, x, d = map(lambda x: int(x) - 1, input().split())
    lst[y][x].append(k)
    players_direction[k] = d

def find(k):
    for i in range(N):
        for j in range(N):
            if k in lst[i][j]:
                idx = lst[i][j].index(k)
                p = lst[i][j][idx:]
                lst[i][j] = lst[i][j][:idx]
                return i, j, p

def play():
    global lst

    for result in range(1, 1001):
        # 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것
        # 하나의 말 위에 다른 말을 올릴 수 있다
        # 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
        for k in range(K):
            y, x, p = find(k)
            d = players_direction[k]

            ny, nx = y + directions[d][0], x + directions[d][1]
            # 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다름
            # 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
            # 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
            if not(0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
                d = directions_oppo[d]
                players_direction[k] = d
                ny, nx = y + directions[d][0], x + directions[d][1]

            # 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는
            # 이동하지 않고 가만히 있는다.
            if not(0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 2:
                ny, nx = y, x
                lst[ny][nx] += p

            elif board[ny][nx] == 0:
                # 흰색인 경우에는 그 칸으로 이동한다.
                # 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
                # A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
                # 예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는
                # A번 말이 이동한 후에는 D, E, A, B, C가 된다.
                lst[ny][nx] += p

            else:
            # 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
                # A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.
                # A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.
                lst[ny][nx] += p[::-1]


            # 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료
            if len(lst[ny][nx]) > 3:
                print(result)
                return

    # 게임이 종료되는 턴의 번호, 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력
    else:
        print(-1)

play()