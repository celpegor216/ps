import heapq


N, M, S, E, C = map(int, input().split())
lst = [[] for _ in range(N + 1)]
MAX = -1
for _ in range(M):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))
    MAX = max(MAX, c)


def check(maxc):
    results = [21e8] * (N + 1)
    results[S] = 0

    q = []
    heapq.heappush(q, (0, 0, S))

    while q:
        cost, max_cost, via = heapq.heappop(q)

        if via == E:
            return 1

        for nxt, nxt_cost in lst[via]:
            nxt_maxc = max(nxt_cost, max_cost)
            if results[nxt] <= cost + nxt_cost or cost + nxt_cost > C or nxt_maxc > maxc:
                continue

            results[nxt] = cost + nxt_cost
            heapq.heappush(q, (cost + nxt_cost, nxt_maxc, nxt))


start, end = 1, MAX + 1
result = -1
while start <= end:
    middle = (start + end) // 2

    if check(middle):
        result = middle
        end = middle - 1
    else:
        start = middle + 1

print(result)