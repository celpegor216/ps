# 힌트: 다익스트라
# 해답 참조

import heapq

V, E = map(int, input().split())
K = int(input())
nodes = [[] for _ in range(V + 1)]
for e in range(E):
    start, end, weight = map(int, input().split())
    nodes[start].append((end, weight))

INF = 21e8

weights = [INF] * (V + 1)
weights[K] = 0

pq = []
heapq.heappush(pq, (0, K)) # (시작 노드에서 경유 노드까지의 비용, 경유 노드)

while pq:
    start_via_weight, via = heapq.heappop(pq)

    if start_via_weight <= weights[via]:
        for item in nodes[via]:
            start_via_target_weight = start_via_weight + item[1]
            if start_via_target_weight < weights[item[0]]:
                weights[item[0]] = start_via_target_weight
                heapq.heappush(pq, (start_via_target_weight, item[0]))

for i in range(1, V + 1):
    if weights[i] == INF:
        print('INF')
    else:
        print(weights[i])