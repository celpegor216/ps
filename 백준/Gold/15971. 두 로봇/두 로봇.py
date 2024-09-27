import heapq, sys
input = sys.stdin.readline


N, S, E = map(int, input().split())
lst = [dict() for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    lst[a][b] = c
    lst[b][a] = c

results = [21e8] * (N + 1)
results[S] = 1

before = [0] * (N + 1)
before[S] = -1

q = []
heapq.heappush(q, (0, S))

while q:
    cost, now = heapq.heappop(q)

    if results[now] < cost or now == E:
        continue

    for nxt, nc in lst[now].items():
        if results[nxt] > cost + nc:
            results[nxt] = cost + nc
            heapq.heappush(q, (cost + nc, nxt))
            before[nxt] = now

total = 0
maxv = 0
now = E
while now != S:
    cost = lst[now][before[now]]
    total += cost
    maxv = max(maxv, cost)
    now = before[now]

print(total - maxv)