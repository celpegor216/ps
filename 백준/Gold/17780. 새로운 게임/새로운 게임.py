# 가장 아래에 있는 말만 이동할 수 있다

N, K = map(int, input().split())
board = [list(map(int, input().split())) + [2] for _ in range(N)] + [[2] * (N + 1)]
players = [[[] for _ in range(N)] for _ in range(N)]

directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
directions_oppo = (1, 0, 3, 2)

for k in range(K):
    y, x, d = map(lambda x: int(x) - 1, input().split())
    players[y][x].append([k, d])


def find(k):
    for i in range(N):
        for j in range(N):
            if players[i][j] and players[i][j][0][0] == k:
                return i, j, players[i][j][0][1]

    return -1, -1, -1


def play():
    for result in range(1, 1001):
        for k in range(K):
            y, x, d = find(k)

            if y == x == d == -1:
                continue

            dy, dx = directions[d]
            ny, nx = y + dy, x + dx

            if board[ny][nx] == 2:
                d = directions_oppo[d]
                players[y][x][0][1] = d
                dy, dx = directions[d]
                ny, nx = y + dy, x + dx

            move_players = [player[:] for player in players[y][x]]
            players[y][x] = []
            if board[ny][nx] == 0:
                players[ny][nx] += move_players
            elif board[ny][nx] == 1:
                players[ny][nx] += move_players[::-1]
            else:
                ny, nx = y, x
                players[ny][nx] += move_players

            if len(players[ny][nx]) > 3:
                return result

    return -1


print(play())
