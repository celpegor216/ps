M, N = map(int, input().split())

# 처음 시작하는 방향이 동쪽이고 왼쪽(반시계방향)으로 회전하므로 동 > 북 > 서 > 남 순서로 작성
directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
d = 0    # 현재 방향
y, x = N - 1, 0    # 현재 위치

# 중복 방문 방지를 위한 배열
used = [[0] * M for _ in range(N)]
used[y][x] = 1
cnt = 1    # 방문한 칸의 개수

# 모든 칸을 방문하면 종료
while cnt < N * M:
    # 현재 방향으로 한 칸 이동
    ny, nx = y + directions[d][0], x + directions[d][1]

    # 이동할 수 없으면 회전해서 한 칸 이동
    if not (0 <= ny < N and 0 <= nx < M and not used[ny][nx]):
        d = (d + 1) % 4
        ny, nx = y + directions[d][0], x + directions[d][1]
    
    used[ny][nx] = 1
    y, x = ny, nx
    cnt += 1

# 남서쪽 모서리는 (0, 0) 남동쪽 모서리는 (N-1, 0), 북동쪽 모서리는 (N-1, M-1)
# x좌표는 그대로 출력해도 되는데 y좌표는 N - y로 출력해야 함
print(x, N - y - 1)