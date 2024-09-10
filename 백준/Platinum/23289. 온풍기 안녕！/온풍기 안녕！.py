from collections import deque

# 크기가 R×C, 모든 칸의 온도가 K 이상이 되었는지 검사
N, M, K = map(int, input().split())
# 가장 처음에 모든 칸의 온도는 0
# 0: 빈 칸
# 1: 방향이 오른쪽인 온풍기가 있음
# 2: 방향이 왼쪽인 온풍기가 있음
# 3: 방향이 위인 온풍기가 있음
# 4: 방향이 아래인 온풍기가 있음
# 5: 온도를 조사해야 하는 칸
# 온풍기는 하나 이상 있고, 온도를 조사해야 하는 칸도 하나 이상
lst = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 온도가 5 이상인지 검사해야 하는 칸의 목록
checklist = []
# 온풍기 위치, 방향
hots = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if lst[i][j] == 5:
            checklist.append((i, j))
        elif lst[i][j]:
            hots.append((i, j, lst[i][j] - 1))
        lst[i][j] = 0

# 오른쪽, 왼쪽, 위쪽, 아래쪽
# 방향 별 다음에 확인해야 하는 좌표, 확인해야 하는 벽
# 바람이 "오른쪽"으로 불었을 때
# 어떤 칸 (x, y)에서 (x-1, y+1)로 바람이 이동할 수 있으려면, (x, y)와 (x-1, y) 사이에 벽이 없어야 하고, (x-1, y)와 (x-1, y+1) 사이에도 벽이 없어야 한다.
# => [[[x, y에서 0번 타입 벽, x-1, y에서 1번 타입 벽]]]
# (x, y)에서 (x, y+1)로 바람이 이동할 수 있으려면 (x, y)와 (x, y+1) 사이에 벽이 없어야 한다.
# => [[[x, y에서 1번 타입 벽]]]
# 마지막으로 (x, y)에서 (x+1, y+1)로 바람이 이동할 수 있으려면, (x, y)와 (x+1, y), (x+1, y)와 (x+1, y+1) 사이에 벽이 없어야 한다.
# => [[[x+1, y에서 0번 타입 벽, x+1, y에서 1번 타입 벽]]]
check_directions = (
    [[-1, 1, [(0, 0, 0), (-1, 0, 1)]], [0, 1, [(0, 0, 1)]], [1, 1, [(1, 0, 0), (1, 0, 1)]]],
    [[-1, -1, [(0, 0, 0), (-1, -1, 1)]], [0, -1, [(0, -1, 1)]], [1, -1, [(1, 0, 0), (1, -1, 1)]]],
    [[-1, -1, [(0, -1, 1), (0, -1, 0)]], [-1, 0, [(0, 0, 0)]], [-1, 1, [(0, 0, 1), (0, 1, 0)]]],
    [[1, -1, [(0, -1, 1), (1, -1, 0)]], [1, 0, [(1, 0, 0)]], [1, 1, [(0, 0, 1), (1, 1, 0)]]],
)
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

# 벽의 개수 W
W = int(input())
# 온풍기가 있는 칸과 바람이 나오는 방향에 있는 칸 사이에는 벽이 없다.
# 온풍기의 바람이 나오는 방향에 있는 칸은 항상 존재한다.
# 세 정수 x, y, t로 이루어져 있다.
# walls[i][j][t]: i, j에 t타입의 벽이 있는지 확인
walls = [[[0] * 2 for _ in range(M + 1)] for _ in range(N + 1)]
for _ in range(W):
    x, y, t = map(int, input().split())

    # t가 0인 경우 (x, y)와 (x-1, y) 사이에 벽이 있는 것이고,
    # 1인 경우에는 (x, y)와 (x, y+1) 사이에 벽이 있는 것
    walls[x][y][t] = 1

result = 0
while 1:
    # 온풍기가 2대 이상 있을 수도 있다
    # 온풍기가 있는 칸도 다른 온풍기에 의해 온도가 상승할 수 있음
    # 이 경우 각각의 온풍기에 의해서 상승한 온도를 모두 합한 값이 해당 칸의 상승한 온도
    changes = [[0] * (M + 1) for _ in range(N + 1)]
    # 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    for sy, sx, d in hots:
        # 온풍기에서 따뜻한 바람이 한 번 나오면, 다음과 같은 영역의 온도가 칸에 적힌 값만큼 증가
        # 어떤 칸 (x, y)에 온풍기 바람이 도착해 온도가 k (> 1)만큼 상승했다면,
        # (x-1, y+1), (x, y+1), (x+1, y+1)의 온도도 k-1만큼 상승
        # 일부 칸과 칸 사이에는 벽이 있어 온풍기 바람이 지나갈 수 없다

        sy += directions[d][0]
        sx += directions[d][1]

        q = deque()
        q.append((sy, sx))
        changes[sy][sx] += 5

        used = [[0] * (M + 1) for _ in range(N + 1)]
        used[sy][sx] = 1
        # 온풍기의 바람이 나오는 방향에 있는 칸은 항상 온도가 5도 올라간다
        for i in range(4, 0, -1):
            if not q:
                break

            for _ in range(len(q)):
                y, x = q.popleft()

                for dy, dx, check_walls in check_directions[d]:
                    ny, nx = y + dy, x + dx

                    if not(0 < ny <= N and 0 < nx <= M) or used[ny][nx]:
                        continue

                    for di, dj, t in check_walls:
                        ni, nj = y + di, x + dj
                        if not(0 < ni <= N and 0 < nj <= M) or walls[ni][nj][t]:
                            break
                    else:
                        changes[ny][nx] += i
                        q.append((ny, nx))
                        used[ny][nx] = 1

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            lst[i][j] += changes[i][j]
            changes[i][j] = 0

    # 온도가 조절됨
    # 모든 인접한 칸에 대해서, 온도가 높은 칸에서 낮은 칸으로 ⌊(두 칸의 온도의 차이)/4⌋만큼 온도가 조절
    # 온도가 높은 칸은 이 값만큼 온도가 감소하고, 낮은 칸은 온도가 상승
    # 인접한 두 칸 사이에 벽이 있는 경우에는 온도가 조절되지 않는다
    for i in range(1, N + 1):
        for j in range(1, M + 1):

            for t, value in enumerate(((-1, 0), (0, 1))):
                dy, dx = value
                ny, nx = i + dy, j + dx
                if walls[i][j][t] or not(0 < ny <= N and 0 < nx <= M) or lst[ny][nx] == lst[i][j]:
                    continue

                diff = abs(lst[i][j] - lst[ny][nx]) // 4
                if lst[i][j] > lst[ny][nx]:
                    changes[i][j] -= diff
                    changes[ny][nx] += diff
                else:
                    changes[i][j] += diff
                    changes[ny][nx] -= diff

    # 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    # 온도가 0인 칸은 온도가 감소하지 않는다.
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            lst[i][j] += changes[i][j]

            if lst[i][j] and (i == 1 or i == N or j == 1 or j == M):
                lst[i][j] -= 1

    # 초콜릿을 하나 먹는다.
    result += 1

    # 먹는 초콜릿의 개수가 100을 넘어가면 101을 출력
    if result > 100:
        break

    # 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사.
    # 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
    for y, x in checklist:
        if lst[y][x] < K:
            break
    else:
        break

print(result)
