N, M = map(int, input().split())
y, x, d = map(int, input().split())
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
lst = [list(map(int, input().split())) for _ in range(N)]

result = 0
used = [[0] * M for _ in range(N)]
while 1:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not used[y][x]:
        used[y][x] = 1
        result += 1

    # 현재 칸의 주변 4칸 중 청소되지 않은 칸이 있는지 확인
    flag = 0
    for i in range(4):
        dy, dx = directions[(d + i) % 4]
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and not used[ny][nx]:
            flag = 1
            break

    # 청소되지 않은 빈 칸이 없는 경우,
    if not flag:
        ny = y - directions[d][0]
        nx = x - directions[d][1]

        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx]:
            y = ny
            x = nx
            continue
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            break

    # 청소되지 않은 빈 칸이 있는 경우,
    else:
        # 반시계 방향으로 90도 회전
        d = (d - 1) % 4
        ny = y + directions[d][0]
        nx = x + directions[d][1]

        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        if 0 <= ny < N and 0 <= nx < M and not lst[ny][nx] and not used[ny][nx]:
            y = ny
            x = nx

print(result)