# 98퍼센트에서 계속 틀림...
# 해답: https://recordofwonseok.tistory.com/324

import heapq

V, E, P = map(int, input().split())

edges = [[] for _ in range(V + 1)]
for e in range(E):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

def dijkstra(start):
    result = [21e8] * (V + 1)
    result[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        start_via_cost, via = heapq.heappop(q)

        for edge in edges[via]:
            target, cost = edge
            start_via_target_cost = start_via_cost + cost
            if result[target] > start_via_target_cost:
                result[target] = start_via_target_cost
                heapq.heappush(q, (start_via_target_cost, target))
    
    return result

if dijkstra(1)[-1] == dijkstra(1)[P] + dijkstra(P)[-1]:
    print('SAVE HIM')
else:
    print('GOOD BYE')