N = 19
used = [[0] * N for _ in range(N)]

Q = int(input())
queries = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

for q in range(Q):
    y, x = queries[q]
    color = q % 2 + 1
    used[y][x] = color

    # 지금 위치 기준 가로로 연결된 같은 색 돌 수
    row_cnt = 1
    for dx in (-1, 1):
        nx = x + dx
        while 0 <= nx < N and used[y][nx] == color:
            row_cnt += 1
            nx += dx
    
    if row_cnt == 5:
        print(q + 1)
        break

    # 지금 위치 기준 세로로 연결된 같은 색 돌 수
    col_cnt = 1
    for dy in (-1, 1):
        ny = y + dy
        while 0 <= ny < N and used[ny][x] == color:
            col_cnt += 1
            ny += dy
    
    if col_cnt == 5:
        print(q + 1)
        break

    # 지금 위치 기준 좌상우하로 연결된 같은 색 돌 수
    lurd_cnt = 1
    for d in (-1, 1):
        ny, nx = y + d, x + d
        while 0 <= ny < N and 0 <= nx < N and used[ny][nx] == color:
            lurd_cnt += 1
            ny += d
            nx += d
    
    if lurd_cnt == 5:
        print(q + 1)
        break

    # 지금 위치 기준 좌하우상으로 연결된 같은 색 돌 수
    ldru_cnt = 1
    for d in (-1, 1):
        ny, nx = y + d, x - d
        while 0 <= ny < N and 0 <= nx < N and used[ny][nx] == color:
            ldru_cnt += 1
            ny += d
            nx -= d
    
    if ldru_cnt == 5:
        print(q + 1)
        break
else:
    print(-1)