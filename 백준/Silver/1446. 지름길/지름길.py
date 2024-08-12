import heapq

N, D = map(int, input().split())
lst = []

for _ in range(N):
    a, b, c = map(int, input().split())

    if b > D:
        continue
    lst.append((a, b, c))

N = len(lst)

lst.sort()

costs = [D] * N
q = []
for n in range(N):
    costs[n] = lst[n][0] + lst[n][2]
    heapq.heappush(q, (costs[n], n))

while q:
    cost, via = heapq.heappop(q)

    for nxt in range(via + 1, N):
        if lst[nxt][0] >= lst[via][1]:
            nxt_cost = cost + lst[nxt][0] - lst[via][1] + lst[nxt][2]
            if nxt_cost < costs[nxt]:
                costs[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

result = D
for n in range(N):
    result = min(result, D - lst[n][1] + costs[n])

print(result)