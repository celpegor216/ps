# 풀이 참조

import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for m in range(M):
    s, e, c = map(int, input().split())

    graph[s].append((e, c))

start, end = map(int, input().split())
INF = 1e8
result = [INF] * (N + 1) # 시작 도시부터 index 도시까지의 비용, 바로 갈 수 없는 경우 INF
result[start] = 0

pq = []
heapq.heappush(pq, (0, start)) # (시작 도시부터 경유 도시까지의 비용, 경유 도시)

while pq:
    start_via_cost, via = heapq.heappop(pq)

    if start_via_cost <= result[via]:
        for item in graph[via]:
            start_via_target_cost = start_via_cost + item[1]
            if start_via_target_cost < result[item[0]]:
                result[item[0]] = start_via_target_cost
                heapq.heappush(pq, (start_via_target_cost, item[0]))

print(result[end])
