N, M = map(int, input().split())

# 달팽이가 오른쪽 > 아래 > 왼쪽 > 위 순서로 방향을 꺾기 때문에
# 그 순서에 맞춰서 배열을 작성해줌
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

y = x = d = 0    # 표의 왼쪽 위 칸에서 오른쪽 방향으로 시작
result = 0    # 방향을 꺾은 횟수
used = [[0] * M for _ in range(N)]    # 방문 표시
used[y][x] = 1    # 시작점 방문 표시
cnt = 1    # 현재까지 방문한 칸의 수(시작점 방문 표시 했으므로 1로 시작)

# 모든 칸을 다 방문할 때까지 수행
while cnt < N * M:
    ny, nx = y + directions[d][0], x + directions[d][1]

    # 현재 방향으로 계속 이동했을 때 표의 범위를 벗어났거나,
    # 표의 범위를 벗어나지는 않았지만 이미 방문한 칸일 경우
    if not (0 <= ny < N and 0 <= nx < M) or used[ny][nx]:
        # 시계방향으로 회전하기 때문에 현재 방향에 + 1을 하고,
        # 4가 될 경우 0으로 바꿔줘야 하므로 % 4 적용
        d = (d + 1) % 4
        result += 1
    # 현재 방향으로 계속 이동했을 때 표의 범위를 벗어나지 않고 아직 방문하지 않았다면 이동
    else:
        used[ny][nx] = 1
        y, x = ny, nx
        cnt += 1

print(result)