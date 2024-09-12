from collections import deque


def transform(x):
    return int(x) - 1


# N×N 크기의 격자, M명의 승객, 초기 연료 F
N, M, F = map(int, input().split())
# 0은 빈칸, 1은 벽 > 패딩을 두를까 고민했는데 나한테는 아직 좀 어렵군
lst = [list(map(int, input().split())) for _ in range(N)]
# 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다.
# 행과 열 번호는 1 이상 N 이하의 자연수
# 운전을 시작하는 칸은 빈칸
by, bx = map(transform, input().split())

# 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호
# 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.
customers = dict()
for _ in range(M):
    sy, sx, ey, ex = map(transform, input().split())
    customers[(sy, sx)] = (ey, ex)


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

def bfs(sy, sx, is_target_end):
    q = deque()
    q.append((sy, sx))

    used = [[0] * N for _ in range(N)]
    used[sy][sx] = 1

    result = 0
    possibles = []
    while q:
        for _ in range(len(q)):
            y, x = q.popleft()

            # 손님을 태우고 목적지까지 이동하는 경우
            if is_target_end and y == ey and x == ex:
                return result, []
            # 태울 손님을 찾는 경우
            elif not is_target_end and (y, x) in customers:
                possibles.append((y, x))
                continue

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not used[ny][nx] and not lst[ny][nx]:
                    q.append((ny, nx))
                    used[ny][nx] = 1

        if not is_target_end and possibles:
            return result, possibles

        # 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0
        result += 1

    return 21e8, possibles


# 여러 승객이 같이 탑승하는 경우는 없다 > 한 승객을 태워 목적지로 이동시키는 일을 M번 반복
for m in range(M):
    # 택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다.
    # 알고리즘 경력이 많은 백준은 특정 위치로 이동할 때 항상 최단경로로만 이동
    # M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다
    # 각 승객은 스스로 움직이지 않으며,
    # 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다
    distance, possibles = bfs(by, bx, 0)
    F -= distance

    # 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다.
    if F <= 0 or not possibles:
        print(-1)
        break

    # 현재 위치에서 최단거리가 가장 짧은 승객
    # 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을,
    # 그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객
    possibles.sort()

    ey, ex = customers.pop(possibles[0])

    # 연료는 한 칸 이동할 때마다 1만큼 소모
    distance, _ = bfs(possibles[0][0], possibles[0][1], 1)

    F -= distance
    # 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다
    # 승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
    if F < 0:
        print(-1)
        break

    # 한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전
    # 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.
    F += distance * 2

    by, bx = ey, ex
else:
    # 모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력
    print(F)