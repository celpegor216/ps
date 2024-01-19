import heapq

N, T = map(int, input().split())
q = []

for _ in range(N):
    w, p = map(int, input().split())

    heapq.heappush(q, (-p, -w))

result = 0

for n in range(N):
    p, w = heapq.heappop(q)
    p, w = -p, -w

    result += w + p * (T - n - 1)

print(result)