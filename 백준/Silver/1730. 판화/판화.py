N = int(input())
cmds = input()

# used[i][j][0]: (i, j) 위치에서 왼쪽 혹은 오른쪽으로 움직인 적이 있는 경우 1 아니면 0
# used[i][j][1]: (i, j) 위치에서 위쪽 혹은 아래쪽으로 움직인 적이 있는 경우 1 아니면 0
used = [[[0] * 2 for _ in range(N)] for _ in range(N)]

# 처음 로봇의 조각도를 올려놓는 위치는 항상 이 점들 중 맨 왼쪽 맨 위의 꼭짓점
y = x = 0
directions = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

for cmd in cmds:
    # 로봇 팔이 격자 바깥으로 나가도록 하는 움직임 명령을 만나면, 무시
    ny, nx = y + directions[cmd][0], x + directions[cmd][1]

    if 0 <= ny < N and 0 <= nx < N:
        if cmd in 'LR':
            used[y][x][0] = 1
        else:
            used[y][x][1] = 1

        y, x = ny, nx

        if cmd in 'LR':
            used[y][x][0] = 1
        else:
            used[y][x][1] = 1

for i in range(N):
    for j in range(N):
        # 로봇팔이 지나지 않은 점은 '.'
        if sum(used[i][j]) == 0:
            print('.', end='')
        # 수직과 수평 방향 모두로 지난 점은 '+'
        elif sum(used[i][j]) == 2:
            print('+', end='')
        # 로봇팔이 수평 방향으로만 지난 점은 '-'
        elif used[i][j][0]:
            print('-', end='')
        # 로봇팔이 수직 방향으로만 지난 점은 '|'
        else:
            print('|', end='')
    print()
