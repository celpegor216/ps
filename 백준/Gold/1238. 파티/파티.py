# 힌트: 다익스트라
# 플로이드-워셜 알고리즘은 시간 복잡도가 O(n^3)으로, 그래프의 크기가 작아 세제곱 시간 알고리즘을 적용해도 문제가 풀릴 때만 사용할 수 있습니다.

import heapq

N, M, X = map(int, input().split())

lst = [[] for _ in range(N + 1)]

for m in range(M):
    s, e, c = map(int, input().split())
    lst[s].append((e, c))

def dijkstra(s, e):
    INF = 10e8
    result = [INF] * (N + 1)
    result[s] = 0

    q = []
    heapq.heappush(q, (0, s))

    while q:
        start_via_cost, via = heapq.heappop(q)
        for target, cost in lst[via]:
            start_via_target_cost = start_via_cost + cost
            if start_via_target_cost < result[target]:
                result[target] = start_via_target_cost
                heapq.heappush(q, (start_via_target_cost, target))

    return result[e]

temp = [0] * (N + 1)

for i in range(1, N + 1):
    temp[i] += dijkstra(i, X) + dijkstra(X, i)

print(max(temp))