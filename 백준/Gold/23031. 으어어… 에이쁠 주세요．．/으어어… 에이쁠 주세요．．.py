# N × N
N = int(input())
cmds = input()
lst = []
zombies = []
for i in range(N):
    tmp = list(input())

    for j in range(N):
        if tmp[j] == 'Z':
            tmp[j] = 'O'
            zombies.append([i, j, 0])

    lst.append(tmp)
Z = len(zombies)

directions = ((1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1), (0, 0))


def check():
    # 가장 왼쪽 위인 (1, 1)에서 출발하고 아리와 학생 좀비들은 모두 아래 방향
    sy = sx = sd = 0

    lights = [[0] * N for _ in range(N)]

    for cmd in cmds:
        # F는 앞으로 1칸 전진
        # L은 아리가 현재 바라보고 있는 방향을 기준으로 왼쪽으로 90도 방향 전환
        # R은 오른쪽으로 90도 방향을 전환
        # N × N 밖으로는 이동할 수 없다. 벽에 부딪히게 되면 전진하지 못하고 제자리에 머문다
        if cmd == 'L':
            sd = (sd - 1) % 4
        elif cmd == 'R':
            sd = (sd + 1) % 4
        else:
            dy, dx = directions[sd]
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < N and 0 <= nx < N:
                sy, sx = ny, nx

        # 아리는 형광등 스위치가 있는 칸에 도착하면 그 곳에 학생 좀비가 있더라도
        # 학생 좀비랑 마주치기 전에 스위치를 켠다
        # 스위치를 켜게 되면 해당 스위치가 있는 칸과 상, 하, 좌, 우, 대각선 네 방향으로
        # 1칸씩 불을 밝힌다. 스위치는 한 번 켜게 되면 꺼지지 않는다
        if lst[sy][sx] == 'S':
            for dy, dx in directions:
                ny, nx = sy + dy, sx + dx
                if 0 <= ny < N and 0 <= nx < N:
                    lights[ny][nx] = 1

        # 아리가 이동을 마칠 때마다 학생 좀비들은 자신이 보고 있는 방향으로 한 칸 전진
        # 학생 좀비들이 벽에 부딪히게 되면 제자리에서 뒤를 돌아 반대 방향을 바라본다
        # 불이 꺼져있는 칸에서 학생 좀비와 함께 있으면 괴담에서 나오는 좀비로 착각하여
        # 그 자리에서 바로 기절해 다음 날 아침에 깨어난다.
        # 하지만 불이 켜져 있는 칸이거나 스위치가 있는 칸에서는
        # 평범한 학생인 것을 알아보고 기절하지 않는다
        for i in range(Z):
            y, x, d = zombies[i]

            if y == sy and x == sx and not lights[sy][sx]:
                return 'Aaaaaah!'

            dy, dx = directions[d]
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                zombies[i][0] = ny
                zombies[i][1] = nx
            else:
                zombies[i][2] = (d + 2) % 4

            if zombies[i][0] == sy and zombies[i][1] == sx and not lights[sy][sx]:
                return 'Aaaaaah!'

    return 'Phew...'


print(check())
