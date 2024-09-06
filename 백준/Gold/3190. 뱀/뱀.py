from collections import deque


# NxN
N = int(input())
M = N
# 사과의 개수
K = int(input())
# 사과의 위치, 1 ~ N
apples = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    i, j = map(int, input().split())
    apples[i][j] = 1
# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
snake = deque()
snake.append((1, 1))
d = 0

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

L = int(input())
moves = []
for _ in range(L):
    x, c = input().split()
    moves.append((int(x), 1 if c == 'D' else -1))
move_idx = 0

result = 0
while 1:
    result += 1

    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    hy, hx = snake[0]
    ny, nx = hy + directions[d][0], hx + directions[d][1]

    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    # 보드의 상하좌우 끝에 벽
    if not(1 <= ny <= N and 1 <= nx <= M) or (ny, nx) in snake:
        print(result)
        break

    snake.appendleft((ny, nx))
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
    # 즉, 몸길이는 변하지 않는다.
    if apples[ny][nx]:
        apples[ny][nx] = 0
    else:
        snake.pop()

    # 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전
    if move_idx < L and moves[move_idx][0] == result:
        d = (d + moves[move_idx][1]) % 4
        move_idx += 1
