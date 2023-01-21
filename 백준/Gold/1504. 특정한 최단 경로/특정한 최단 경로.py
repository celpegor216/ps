# 힌트: 다익스트라
# 해답: https://pottatt0.tistory.com/134

import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())

INF = 10e8
lst = [[] for _ in range(N + 1)]
for e in range(E):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    result = [INF] * (N + 1)
    result[start] = 0

    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        start_via_cost, via = heapq.heappop(hq)

        if start_via_cost <= result[via]:
            for target, cost in lst[via]:
                start_via_target_cost = start_via_cost + cost
                if start_via_target_cost < result[target]:
                    result[target] = start_via_target_cost
                    heapq.heappush(hq, (start_via_target_cost, target))

    return result[end]

v1v2 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
v2v1 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

print(min(v1v2, v2v1) if v1v2 < INF and v2v1 < INF else -1)