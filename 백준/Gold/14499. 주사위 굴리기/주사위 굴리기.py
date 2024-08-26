N, M, y, x, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

directions = ((0, 1), (0, -1), (-1, 0), (1, 0))    # 동서북남
dice_directions = (
    # 동쪽으로 굴리면 0상 1북 2동 3서 4남 5하 > 3서 1북 0상 5하 4남 2동
    (3, 1, 0, 5, 4, 2),
    # 서쪽으로 굴리면 0상 1북 2동 3서 4남 5하 > 2동 1북 5하 0상 4남 3서
    (2, 1, 5, 0, 4, 3),
    # 북쪽으로 굴리면 0상 1북 2동 3서 4남 5하 > 4남 0상 2동 3서 5하 1북
    (4, 0, 2, 3, 5, 1),
    # 남쪽으로 굴리면 0상 1북 2동 3서 4남 5하 > 1북 5하 2동 3서 0상 4남
    (1, 5, 2, 3, 0, 4),
)


dice = [0] * 6    # 상 북 동 서 남 하

for cmd in cmds:
    cmd -= 1

    ny, nx = y + directions[cmd][0], x + directions[cmd][1]

    # 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
    if not (0 <= ny < N and 0 <= nx < M):
        continue

    y, x = ny, nx

    # 주사위 굴리기
    dice = [dice[x] for x in dice_directions[cmd]]

    # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
    # 칸에 쓰여 있는 수는 0이 된다.
    if lst[y][x]:
        dice[5] = lst[y][x]
        lst[y][x] = 0
    # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
    elif dice[5] and not lst[y][x]:
        lst[y][x] = dice[5]

    # 이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다.
    print(dice[0])