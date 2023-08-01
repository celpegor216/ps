# 시간 초과 해결 힌트: https://www.acmicpc.net/board/view/102609

import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
is_visible = list(map(int, input().split()))
edges = [[] for _ in range(N)]

for m in range(M):
    a, b, t = map(int, input().split())

    if (a != N - 1 and is_visible[a]) or (b != N - 1 and is_visible[b]):
        continue

    edges[a].append((b, t))
    edges[b].append((a, t))

q = []

result = [10 ** 12] * N
result[0] = 0

heapq.heappush(q, (0, 0))

while q:
    start_via_cost, via = heapq.heappop(q)

    if result[via] < start_via_cost:
        continue

    for target, cost in edges[via]:
        start_via_target_cost = start_via_cost + cost
        if start_via_target_cost < result[target]:
            result[target] = start_via_target_cost
            heapq.heappush(q, (start_via_target_cost, target))

if result[-1] == 10 ** 12:
    print(-1)
else:
    print(result[-1])