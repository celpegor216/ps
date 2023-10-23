import heapq

N = int(input())
friends = list(map(int, input().split()))
M = int(input())
lst = [[] for _ in range(N + 1)]

for m in range(M):
    a, b, c = map(int, input().split())

    lst[a].append((b, c))
    lst[b].append((a, c))

results = [[21e8] * (N + 1) for _ in range(3)]

for i in range(3):
    q = []
    heapq.heappush(q, (0, friends[i]))
    
    while q:
        start_via_cost, via = heapq.heappop(q)
        for target, cost in lst[via]:
            if results[i][target] > start_via_cost + cost:
                results[i][target] = start_via_cost + cost
                heapq.heappush(q, (start_via_cost + cost, target))

resultv = 0
resultn = 0

for n in range(1, N + 1):
    minv = min(results[0][n], results[1][n], results[2][n])

    if resultv < minv:
        resultv = minv
        resultn = n

print(resultn)