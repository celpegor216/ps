import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
start, end = map(int, input().split())
lst = [[] for _ in range(N)]

for _ in range(E):
    s, e, c = map(int, input().split())

    lst[s].append((e, c))
    lst[e].append((s, c))

result = [0] * N
result[start] = 21e8

q = []
heapq.heappush(q, (21e8, start))

while q:
    nowc, nown = heapq.heappop(q)

    for target, cost in lst[nown]:
        minv = min(nowc, cost)
        if result[target] < minv:
            result[target] = minv
            heapq.heappush(q, (minv, target))

print(result[end])