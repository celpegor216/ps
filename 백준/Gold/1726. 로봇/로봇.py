from collections import deque

N, M = map(int, input().split())
# 0은 궤도가 깔려 있어 로봇이 갈 수 있는 지점이고, 1은 궤도가 없어 로봇이 갈 수 없는 지점
lst = [list(map(int, input().split())) for _ in range(N)]
def func(x):
    return int(x) - 1
# 로봇의 현재 위치와 바라보는 방향
sy, sx, sd = map(func, input().split())
# 로봇의 도착 위치와 바라보는 방향
ey, ex, ed = map(func, input().split())

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
turn_left = (3, 2, 0, 1)
turn_right = (2, 3, 1, 0)

q = deque()
q.append((0, sy, sx, sd))
used = [[[0] * 4 for _ in range(M)] for _ in range(N)]
used[sy][sx][sd] = 1

while q:
    cnt, y, x, d = q.popleft()

    # 최소 몇 번의 명령이 필요한지 구하는 프로그램
    # 출발지점에서 도착지점까지는 항상 이동이 가능
    if y == ey and x == ex and d == ed:
        print(cnt)
        break

    # 명령 1. Go k: k는 1, 2 또는 3일 수 있다. 현재 향하고 있는 방향으로 k칸 만큼 움직인다.
    for k in range(1, 4):
        ny, nx = y + directions[d][0] * k, x + directions[d][1] * k
        if not(0 <= ny < N and 0 <= nx < M) or lst[ny][nx]:
            break
        if not used[ny][nx][d]:
            used[ny][nx][d] = 1
            q.append((cnt + 1, ny, nx, d))

    # 명령 2. Turn dir: dir은 left 또는 right 이며, 각각 왼쪽 또는 오른쪽으로 90° 회전한다.
    if not used[y][x][turn_left[d]]:
        used[y][x][turn_left[d]] = 1
        q.append((cnt + 1, y, x, turn_left[d]))
    if not used[y][x][turn_right[d]]:
        used[y][x][turn_right[d]] = 1
        q.append((cnt + 1, y, x, turn_right[d]))