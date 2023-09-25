import heapq

N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]

for n in range(N - 1):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

dp = [[]]

for n in range(1, N + 1):
    result = [21e8] * (N + 1)
    result[n] = 0

    q = []
    heapq.heappush(q, (0, n))
    while q:
        start_via_cost, via = heapq.heappop(q)

        for target, cost in lst[via]:
            start_via_target_cost = start_via_cost + cost
            if result[target] > start_via_target_cost:
                result[target] = start_via_target_cost
                heapq.heappush(q, (start_via_target_cost, target))
    
    dp.append(result)

for m in range(M):
    a, b = map(int, input().split())
    print(dp[a][b])