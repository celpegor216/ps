import heapq
import sys
input = sys.stdin.readline

N, M, A, B, C = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

results = [[21e8] * 2 for _ in range(N + 1)]
results[A] = [0, 0]

q = []
heapq.heappush(q, (0, 0, A))

while q:
    maxv, totalv, via = heapq.heappop(q)

    if results[via][0] < maxv or (results[via][0] == maxv and results[via][1] < totalv):
        continue

    for target, cost in lst[via]:
        tmp = max(maxv, cost)
        if totalv + cost <= C and (results[target][0] > tmp or (results[target][0] == tmp and results[target][1] > totalv + cost)):
            results[target][0] = tmp
            results[target][1] = totalv + cost
            heapq.heappush(q, (results[target][0], results[target][1], target))

if results[B][1] == 21e8:
    print(-1)
else:
    print(results[B][0])