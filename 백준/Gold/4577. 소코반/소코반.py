tc = 0

while 1:
    tc += 1
    N, M = map(int, input().split())

    if N == M == 0:    # 입력의 마지막 줄에는 0 0이 주어짐
        break

    lst = [list(input()) for _ in range(N)]

    y = x = -1
    incomplete = 0

    for n in range(1, N - 1):    # 가장 바깥쪽 칸은 항상 벽
        for m in range(1, M - 1):
            if lst[n][m] in 'wW':
                y = n
                x = m
                lst[n][m] = '.' if lst[n][m] == 'w' else '+'
            elif lst[n][m] == 'b':
                incomplete += 1

    commands = input()
    directions = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

    for command in commands:
        dy, dx = directions[command]
        ny, nx = y + dy, x + dx

        if lst[ny][nx] in '.+':    # 빈 공간, 비어 있는 목표점인 경우 이동
            y = ny
            x = nx
        elif lst[ny][nx] == '#':    # 벽인 경우 이동 못 함
            continue
        else:                       # 박스인 경우 박스가 밀려서 이동할 수 있는지 확인
            bny, bnx = ny + dy, nx + dx
            if lst[bny][bnx] in '#bB':
                continue

            # 박스의 도착지가 목표점이라면
            if lst[bny][bnx] == '+':
                lst[bny][bnx] = 'B'
                incomplete -= 1
            else:
                lst[bny][bnx] = 'b'

            # 박스가 목표점 위에 있었다면
            if lst[ny][nx] == 'B':
                lst[ny][nx] = '+'
                incomplete += 1
            else:
                lst[ny][nx] = '.'

            y = ny
            x = nx

        if not incomplete:
            break

    lst[y][x] = 'w' if lst[y][x] != '+' else 'W'

    print(f'Game {tc}:', 'incomplete' if incomplete else 'complete')
    for line in lst:
        print(''.join(line))