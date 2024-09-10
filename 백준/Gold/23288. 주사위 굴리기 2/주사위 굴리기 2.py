from collections import deque


# 크기가 N×M, 이동하는 횟수 K
N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며
# 놓여져 있는 곳의 좌표는 (1, 1)
# 가장 처음에 주사위의 이동 방향은 동쪽
# 위 - 상 - 우 - 좌 - 하 - 아래
dice = [1, 2, 3, 4, 5, 6]
y = x = d = 0

# 이동 방향 반대로 하려면 (d + 2) % 2
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
directions_dice = [
    # 오른쪽으로 움직이면 0위 1상 2우 3좌 4하 5아래 > 3좌 1상 0위 5아래 4하 2우
    [3, 1, 0, 5, 4, 2],
    # 아래쪽으로 움직이면 0위 1상 2우 3좌 4하 5아래 > 1상 5아래 2우 3좌 0위 4하
    [1, 5, 2, 3, 0, 4],
    # 왼쪽으로 움직이면 0위 1상 2우 3좌 4하 5아래 >  2우 1상 5아래 0위 4하 3좌
    [2, 1, 5, 0, 4, 3],
    # 위쪽으로 움직이면 0위 1상 2우 3좌 4하 5아래 >  4하 0위 2우 3좌 5아래 1상
    [4, 0, 2, 3, 5, 1],
]

# (x, y)에 있는 정수를 B라고 했을때, (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다 => bfs로 미리 구해둬야겠군
# 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다
# 여기서 점수는 B와 C를 곱한 값
scores = [[0] * M for _ in range(N)]

def fill_scores():
    for i in range(N):
        for j in range(M):
            if scores[i][j]:
                continue

            q = deque()
            q.append((i, j))
            used = [[0] * M for _ in range(N)]
            used[i][j] = 1

            idx = 0
            while idx < len(q):
                y, x = q[idx]
                idx += 1

                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and not used[ny][nx] and lst[ny][nx] == lst[i][j]:
                        used[ny][nx] = 1
                        q.append((ny, nx))

            score = len(q) * lst[i][j]
            while q:
                y, x = q.popleft()
                scores[y][x] = score

fill_scores()

result = 0
for _ in range(K):
    # 주사위가 이동 방향으로 한 칸 굴러간다.
    dy, dx = directions[d]

    # 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    if not(0 <= y + dy < N and 0 <= x + dx < M):
        d = (d + 2) % 4
        dy, dx = directions[d]

    y += dy
    x += dx

    dice = [dice[idx] for idx in directions_dice[d]]

    # 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    result += scores[y][x]

    # 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다.
    # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    # A = B인 경우 이동 방향에 변화는 없다.
    if dice[-1] > lst[y][x]:
        d = (d + 1) % 4
    elif dice[-1] < lst[y][x]:
        d = (d - 1) % 4


# 각 이동에서 획득하는 점수의 합
print(result)