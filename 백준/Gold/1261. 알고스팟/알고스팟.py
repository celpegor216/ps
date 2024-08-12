import heapq

M, N = map(int, input().split())
lst = [input() for _ in range(N)]

q = []
heapq.heappush(q, (0, 0, 0))

result = N * M
used = [[result] * M for _ in range(N)]
used[0][0] = 0

while q:
    cnt, y, x = heapq.heappop(q)

    if used[y][x] < cnt:
        continue

    if y == N - 1 and x == M - 1:
        result = min(result, cnt)
        continue

    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            nxt_cnt = cnt + 1 if lst[ny][nx] == '1' else cnt
            if used[ny][nx] > nxt_cnt:
                used[ny][nx] = nxt_cnt
                heapq.heappush(q, (nxt_cnt, ny, nx))

print(result)