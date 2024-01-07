import heapq
import sys
input = sys.stdin.readline

N, M, S, E, C = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, input().split())

    lst[a].append((b, c))
    lst[b].append((a, c))

result = [[21e10, 21e10] for _ in range(N + 1)]
result[S] = [0, 0]

q = []
heapq.heappush(q, (0, 0, S))

while q:
    c, totalc, via = heapq.heappop(q)

    if result[via][0] < c:
         continue

    for target, cost in lst[via]:
        move = totalc + cost
        maxc = max(c, cost)

        if move <= C and maxc < result[target][0]:
                result[target][0] = maxc
                result[target][1] = move
                heapq.heappush(q, (maxc, move, target))

if result[E][1] == 21e10:
    print(-1)
else:
    print(result[E][0])