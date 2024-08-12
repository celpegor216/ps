import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
findable = list(map(int, input().split()))
lst = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, input().split())
    lst[a].append((t, b))
    lst[b].append((t, a))

q = []
heapq.heappush(q, (0, 0))    # 0번째 분기점에서 시작

MAXV = 21e21
result = [MAXV] * N
result[0] = 0

while q:
    cost, via = heapq.heappop(q)

    if cost > result[via]:
        continue

    if via == N - 1:    # 도착지
        continue

    for nxt_cost, nxt in lst[via]:
        if nxt != N - 1 and findable[nxt]:
            continue

        if cost + nxt_cost >= result[nxt]:
            continue

        heapq.heappush(q, (cost + nxt_cost, nxt))
        result[nxt] = cost + nxt_cost

print(result[-1] if result[-1] != MAXV else -1)