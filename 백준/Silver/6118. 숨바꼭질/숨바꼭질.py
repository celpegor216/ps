import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

result = [21e8] * (N + 1)
result[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    cost, now = heapq.heappop(q)

    for target in lst[now]:
        if result[target] > cost + 1:
            result[target] = cost + 1
            heapq.heappush(q, (cost + 1, target))

maxv = 0
maxn = []

for n in range(2, N + 1):
    if result[n] > maxv:
        maxv = result[n]
        maxn = [n]
    elif result[n] == maxv:
        maxn.append(n)

print(maxn[0], maxv, len(maxn))