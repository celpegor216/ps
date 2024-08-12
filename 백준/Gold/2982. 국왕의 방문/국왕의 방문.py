import heapq

N, M = map(int, input().split())
S, E, K, G = map(int, input().split())
king_moves = list(map(int, input().split()))

MAXV = 21e8
lst = [[[MAXV] * 3 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    u, v, l = map(int, input().split())
    lst[u][v][0] = l
    lst[v][u][0] = l

time = 0
for g in range(1, G):
    now = king_moves[g - 1]
    nxt = king_moves[g]
    lst[now][nxt][1] = time
    lst[now][nxt][2] = time + lst[now][nxt][0] - 1
    lst[nxt][now][1] = time
    lst[nxt][now][2] = time + lst[now][nxt][0] - 1
    time += lst[now][nxt][0]

# 상근이 이동
result = [MAXV] * (N + 1)
result[S] = K

q = []
heapq.heappush(q, (K, S))

while q:
    time, via = heapq.heappop(q)

    if via == E:
        continue

    for nxt in range(1, N + 1):
        if lst[via][nxt][0] == MAXV:
            continue

        # 왕이 지나간 길 + 왕이 지나갈 때 상근이도 지나감
        if lst[via][nxt][1] != MAXV and (lst[via][nxt][1] <= time <= lst[via][nxt][2]):
            nxt_time = lst[via][nxt][2] + 1 + lst[via][nxt][0]
        else:
            nxt_time = time + lst[via][nxt][0]

        if result[nxt] > nxt_time:
            result[nxt] = nxt_time
            heapq.heappush(q, (nxt_time, nxt))

print(result[E] - K)
