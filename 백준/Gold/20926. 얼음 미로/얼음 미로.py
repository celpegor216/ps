import heapq


M, N = map(int, input().split())
lst = []
sy = sx = -1
for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j].isdigit():
            tmp[j] = int(tmp[j])
        elif tmp[j] == 'T':
            sy, sx = i, j
            tmp[j] = 0
        elif tmp[j] == 'H':    # 구멍, 만나면 죽음
            tmp[j] = -1
        elif tmp[j] == 'R':    # 바위, 만나면 멈춤
            tmp[j] = -2
        elif tmp[j] == 'E':    # 탈출
            tmp[j] = -3
    lst.append(tmp)


used = [[21e8] * M for _ in range(N)]
used[sy][sx] = 0
q = []
heapq.heappush(q, (0, sy, sx))

result = 21e8
while q:
    t, y, x = heapq.heappop(q)
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        nt = t

        while 0 <= ny < N and 0 <= nx < M and lst[ny][nx] >= 0:
            nt += lst[ny][nx]
            ny += dy
            nx += dx

        # 절벽으로 떨어지거나 구멍에 빠진 경우
        if not (0 <= ny < N and 0 <= nx < M) or lst[ny][nx] == -1:
            continue

        if lst[ny][nx] == -3:
            result = min(result, nt)
            continue

        ny -= dy
        nx -= dx

        # 도착한 곳까지 걸린 미끌 시간이 더 오래 걸린 경우
        if used[ny][nx] <= nt:
            continue

        used[ny][nx] = nt
        heapq.heappush(q, (nt, ny, nx))


print(result if result != 21e8 else -1)