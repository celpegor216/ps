import heapq


# N * N, 오작교 주기 K
N, K = map(int, input().split())

# 0: 건널 수 없는 절벽
# 1: 이동할 수 있는 일반적인 땅
# 2 이상의 수: 적혀있는 수 만큼의 주기를 가지는 오작교
lst = [list(map(int, input().split())) for _ in range(N)]

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

def find():
    # 견우의 시작점은 지형의 맨 왼쪽 위 (0, 0) 이고,
    # 직녀가 사는 곳은 지형의 맨 오른쪽 아래인 (N-1, N-1)
    # 견우가 시작점에서 출발하는 시간은 0분
    # 안전을 위해 두 번 연속으로 오작교를 건너지는 않기로 했다
    q = []
    heapq.heappush(q, (0, 0, 0))

    used = [[21e8] * N for _ in range(N)]
    used[0][0] = 0

    while q:
        time, y, x = heapq.heappop(q)

        if y == x == N - 1:
            return time

        if used[y][x] < time:
            continue

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if not(0 <= ny < N and 0 <= nx < N) or not lst[ny][nx]:
                continue

            nxt_time = time + 1
            if lst[ny][nx] > 1:
                if lst[y][x] > 1:
                    continue

                nxt_time = time - (time % lst[ny][nx]) + lst[ny][nx]

            if used[ny][nx] <= nxt_time:
                continue

            used[ny][nx] = nxt_time
            heapq.heappush(q, (nxt_time, ny, nx))


    return 21e8


result = 21e8
for i in range(N):
    for j in range(N):
        if lst[i][j]:
            continue

        lst[i][j] = K
        result = min(result, find())
        lst[i][j] = 0

print(result)