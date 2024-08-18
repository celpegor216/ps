import heapq

N, M = map(int, input().split())
q = list(map(int, input().split()))

heapq.heapify(q)

for _ in range(M):
    a, b = heapq.heappop(q), heapq.heappop(q)
    heapq.heappush(q, a + b)
    heapq.heappush(q, a + b)

print(sum(q))