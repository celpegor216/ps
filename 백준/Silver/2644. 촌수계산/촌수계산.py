import heapq

N = int(input())
A, B = map(int, input().split())
M = int(input())
lst = [[0] * N for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())

    lst[a - 1][b - 1] = 1
    lst[b - 1][a - 1] = 1

INF = 21e8
result = [INF] * N

q = []
heapq.heappush(q, (0, A - 1))

while q:
    start_via_cost, via = heapq.heappop(q)

    for i in range(N):
        if result[i] == INF and lst[via][i]:
            result[i] = start_via_cost + 1
            heapq.heappush(q, (start_via_cost + 1, i))

print(result[B - 1] if result[B - 1] != INF else -1)