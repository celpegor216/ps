import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

S, T = map(int, input().split())

result = [21e8] * (N + 1)
result[S] = 0

q = []
heapq.heappush(q, (0, S))

while q:
    cost, via = heapq.heappop(q)

    if result[via] < cost:
        continue

    for target, c in lst[via]:
        if result[target] > cost + c:
            result[target] = cost + c
            heapq.heappush(q, (result[target], target))

print(result[T])