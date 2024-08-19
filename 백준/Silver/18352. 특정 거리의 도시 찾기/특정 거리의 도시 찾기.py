import heapq, sys
input = sys.stdin.readline

N, M, K, S = map(int, input().split())
lst = [set() for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    lst[A].add(B)

results = [21e8] * (N + 1)
results[S] = 0

q = []
heapq.heappush(q, (0, S))

while q:
    cost, via = heapq.heappop(q)

    for nxt in lst[via]:
        if results[nxt] > cost + 1:
            results[nxt] = cost + 1
            heapq.heappush(q, (cost + 1, nxt))

result = []
for i in range(1, N + 1):
    if results[i] == K:
        result.append(i)

if result:
    for item in result:
        print(item)
else:
    print(-1)