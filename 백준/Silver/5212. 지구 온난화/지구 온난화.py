# 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다
# 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다
# 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

# 50년 뒤 지도의 크기
miny = minx = N * M
maxy = maxx = -1

# 50년 뒤 지도에 표시될 좌표
result = [['.'] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        if lst[n][m] == '.':
            continue

        cnt = 4    # 인접한 바다의 수
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = n + dy, m + dx
            if 0 <= ny < N and 0 <= nx < M and lst[ny][nx] == 'X':
                cnt -= 1

        if cnt < 3:
            result[n][m] = 'X'
            miny = min(miny, n)
            minx = min(minx, m)
            maxy = max(maxy, n)
            maxx = max(maxx, m)

for line in result[miny:maxy + 1]:
    print(''.join(line[minx:maxx + 1]))