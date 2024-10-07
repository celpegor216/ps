transform = lambda x: int(x) - 1

char_to_d = {'U': 0, 'R': 1, 'D': 2, 'L': 3, 'S': 4}
directions = ((-1, 0), (0, 1), (1, 0), (0, -1), (0, 0))

N = int(input())
cmds = input()
sy, sx = map(transform, input().split())
walls = [[0] * N for _ in range(N)]
W = int(input())
for _ in range(W):
    y, x = map(transform, input().split())
    walls[y][x] = 1
Z = int(input())
zombies = []
for _ in range(Z):
    y, x, t, d, s = input().split()
    d = char_to_d[d]
    y = transform(y)
    x = transform(x)
    t = int(t)
    s = int(s)
    zombies.append([y, x, t, d, s])
D = int(input())


def move_zombies(zombies):
    new_zombies = []

    # 좀비들의 이동 순서는 생성(입력)된 순
    # 좀비가 이동 중에 플레이어를 만나도 플레이어를 죽이지 않는다
    for y, x, t, d, s in zombies:
        # 하급 좀비는 매일 현재 바라보고 있는 방향으로 한 칸씩 s번 이동한다.
        # 단, 이동하려는 위치가 게임 필드를 벗어나거나 벽인 경우에는
        # s번을 다 이동하지 않고 정지한 뒤, 현재 방향의 반대로 방향을 튼다.
        # 남은 이동 횟수 만큼 다시 이동하지 않음에 유의하라.
        if not t:
            dy, dx = directions[d]
            ny, nx = y, x
            for _ in range(s):
                ny += dy
                nx += dx
                if not(0 <= ny < N and 0 <= nx < N) or walls[ny][nx]:
                    ny -= dy
                    nx -= dx
                    d = (d + 2) % 4
                    break
            new_zombies.append([ny, nx, t, d, s])

        # 상급 좀비는 매일 현재 바라보고 있는 방향으로 한 칸씩 s번 이동한다.
        # 단, 이동하려는 위치가 게임 필드를 벗어나거나 벽인 경우에는 s번을 다 이동하지 않고 정지한다.
        # 벽에 막혔을 경우 벽 앞에서 정지하며, 좀비가 벽을 부숴서 그 벽은 사라진다.
        # 그 후, 중간에 정지했는지 여부와 관계없이 정지한 뒤,
        # 상하좌우 방향 중 벽의 개수를 세어 벽이 가장 많은 방향으로 방향을 튼다.
        # 상급 좀비가 벽의 개수를 셀 때는 해당 상급 좀비가 벽을 무시하고
        # 게임 필드 경계까지 이동했을 때, 만나게 되는 벽의 개수를 센다.
        # 만약 벽의 개수가 같은 경우는 '상', '우', '하', '좌' 우선 순위로 방향을 튼다.
        else:
            dy, dx = directions[d]
            ny, nx = y, x
            for _ in range(s):
                ny += dy
                nx += dx
                if not (0 <= ny < N and 0 <= nx < N):
                    ny -= dy
                    nx -= dx
                    break
                elif walls[ny][nx]:
                    walls[ny][nx] = 0
                    ny -= dy
                    nx -= dx
                    break

            # 벽의 개수 내림차순, 방향 우선순위 오름차순
            selected = (21e8, 21e8)
            for nd in range(4):
                dy, dx = directions[nd]
                ty, tx = ny + dy, nx + dx
                cnt = 0
                while 0 <= ty < N and 0 <= tx < N:
                    cnt += walls[ty][tx]
                    ty += dy
                    tx += dx
                selected = min(selected, (-cnt, nd))

            new_zombies.append([ny, nx, t, selected[1], s])

    return new_zombies


def play(sy, sx, zombies):
    for day in range(D):
        cmd = cmds[day]
        d = char_to_d[cmd]
        dy, dx = directions[d]
        ny, nx = sy + dy, sx + dx

        # 이동하려는 위치가 게임 필드를 벗어나거나 벽인 경우에는 이동하지 않는다
        if 0 <= ny < N and 0 <= nx < N and not walls[ny][nx]:
            sy, sx = ny, nx

        # 플레이어의 명령어 실행이 끝나면 좀비들이 정해진 순서로 한 번에 한 마리씩 이동한다
        zombies = move_zombies(zombies)

        for y, x, _, _, _ in zombies:
            if sy == y and sx == x:
                print(day + 1)
                print('DEAD...')
                return

    print('ALIVE!')


play(sy, sx, zombies)