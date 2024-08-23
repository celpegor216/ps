N, M = map(int, input().split())
# N * N 크기, lst[i][j]: 해당 위치의 바구니에 저장된 물의 양
# 행과 열이 순환함(1번행 위에 N번행, N번행 아래에 1번행) > oob 체크할 필요 없음
lst = [list(map(int, input().split())) for _ in range(N)]

# 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# 대각선 방향
nxt_directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

# 초기 구름
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

for _ in range(M):
    D, S = map(int, input().split())
    D -= 1

    # 모든 구름이 di 방향으로 si칸 이동한다.
    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for i in range(len(clouds)):
        y = (clouds[i][0] + directions[D][0] * S) % N
        x = (clouds[i][1] + directions[D][1] * S) % N
        clouds[i] = (y, x)
        lst[y][x] += 1

    new_lst = [line[:] for line in lst]

    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
    # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    # 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
    # > oob 체크 필요
    for y, x in clouds:
        for dy, dx in nxt_directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and lst[ny][nx]:
                new_lst[y][x] += 1

    lst = new_lst

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    new_clouds = []
    for i in range(N):
        for j in range(N):
            if lst[i][j] > 1 and (i, j) not in clouds:
                new_clouds.append((i, j))
                lst[i][j] -= 2

    clouds = new_clouds

# M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
result = 0

for i in range(N):
    for j in range(N):
        result += lst[i][j]

print(result)