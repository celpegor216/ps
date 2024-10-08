import heapq


# 화물차가 진입하려는 방향으로 파란불이 켜져 있을 때만 교차로로 들어갈 수 있다.
# 그러나 교차로에 들어간 차량은 언제든지 임의의 방향으로 나갈 수 있다
# 교차로의 신호등은 동서 방향과 남북 방향, 두 개의 신호가 주기적으로 켜진다
# 출발지 창고에서 배송지 창고까지 최단 경로
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def find(sy, sx, ey, ex):
    q = []
    heapq.heappush(q, (0, sy, sx))

    used = [[21e8] * M for _ in range(N)]
    used[sy][sx] = 0

    while q:
        time, y, x = heapq.heappop(q)

        if used[y][x] < time:
            continue

        if y == ey and x == ex:
            return time

        for d in range(4):
            dy, dx = directions[d]
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] != '.':
                nxt_time = -1

                if lst[ny][nx] == '#':
                    nxt_time = time + 1
                else:
                    t, a, b = signs[lst[ny][nx]]
                    cycle = a + b
                    now_time = time % cycle
                    now_side = t
                    # 좌우가 먼저 켜지는 경우
                    if t == 0 and now_time >= a:
                        now_time -= a
                        now_side = 1
                    elif t == 1 and now_time >= b:
                        now_time -= b
                        now_side = 0

                    nxt_time = time + 1
                    # 가려는 방향이 상하인 경우, 현재 좌우가 켜져있으면 기다렸다 이동
                    if d % 2 and now_side == 0:
                        nxt_time += (a - now_time)
                    # 가려는 방향이 좌우인 경우, 현재 상하가 켜져있다면 기다렸다 이동
                    elif not d % 2 and now_side == 1:
                        nxt_time += (b - now_time)

                if used[ny][nx] > nxt_time:
                    used[ny][nx] = nxt_time
                    heapq.heappush(q, (nxt_time, ny, nx))

    return 'impossible'


while 1:
    N, M = map(int, input().split())

    if not N:
        break

    lst = []

    sy = sx = ey = ex = -1
    S = 0

    # 'A'는 출발지 창고를 나타내고, 지도에서 유일하다.
    # 'B'는 배송지 창고를 나타내고, 지도에서 유일하다.
    # '.'은 차가 들어갈 수 없는 곳을 나타낸다.
    # '#'은 각 도로 셀을 나타낸다.
    # '#'은 기껏해야 두 개의 다른 도로 셀, 또는 교차로, 창고와 인접하다.
    # 숫자 [0-9]는 신호등에 의해 제어되는 교차로, 교차로는 적어도 세 개의 도로 셀과 인접
    # 번호 k를 가진 교차로가 있으면, 반드시 0부터 k까지 번호를 가진 교차로가 존재
    for i in range(N):
        tmp = list(input())
        for j in range(M):
            if tmp[j] == 'A':
                sy, sx = i, j
                tmp[j] = '#'
            elif tmp[j] == 'B':
                ey, ex = i, j
                tmp[j] = '#'
            elif tmp[j] not in '.#':
                tmp[j] = int(tmp[j])
                S += 1
        lst.append(tmp)

    # 시작 방향(0은 동서, 1은 남북), 동서 시간, 남북 시간
    signs = []
    for i in range(S):
        _, t, a, b = input().split()
        signs.append([0 if t == '-' else 1, int(a), int(b)])

    input()

    print(find(sy, sx, ey, ex))