# 해답: https://velog.io/@j_aion/%EB%B0%B1%EC%A4%80-22870-%EC%82%B0%EC%B1%85


import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append((c, b))
    lst[b].append((c, a))
S, E = map(int, input().split())

for n in range(1, N + 1):
    lst[n].sort(key=lambda x: x[1])

def dijkstra(used, start):
    results = [21e8] * (N + 1)
    results[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, via = heapq.heappop(q)

        if results[via] < cost:
            continue

        for c, nxt in lst[via]:
            if nxt in used:
                continue

            if cost + c < results[nxt]:
                results[nxt] = cost + c
                heapq.heappush(q, (cost + c, nxt))

    return results

# S ~ E 까지 최소 이동 과정에서 거쳐간 노드 찾기
# nxt ~ E 거리를 구해야 하므로 distances를 구할 때 E를 시작점으로 해야 함
distances = dijkstra(set(), E)
cost = 0
via = S
used = set()
while via != E:
    for c, nxt in lst[via]:
        # S ~ via 거리 + via ~ nxt 거리 + nxt ~ E 거리가 S ~ E 최단 거리와 같다면
        # S ~ E 최소 이동 과정에서 nxt를 거쳐간 것
        if cost + c + distances[nxt] == distances[S]:
            cost += c
            used.add(nxt)
            via = nxt
            break

# 사용한 노드를 제외하고 S ~ E까지 다시 최소 이동
used.remove(E)
distances = dijkstra(used, S)

print(cost + distances[E])