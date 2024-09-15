import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
P = 11
positions = [[] for _ in range(P + 1)]

for _ in range(N):
    p, w = map(int, input().split())
    heapq.heappush(positions[p], -w)

for _ in range(K):
    for p in range(1, P + 1):
        if positions[p]:
            heapq.heappush(positions[p], heapq.heappop(positions[p]) + 1)

result = 0
for p in range(1, P + 1):
    if positions[p]:
        result -= positions[p][0]

print(result)