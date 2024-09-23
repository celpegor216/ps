import heapq


N = int(input())
lst = [[] for _ in range(N + 1)]

while 1:
    a, b = map(int, input().split())

    if a == -1:
        break

    lst[a].append(b)
    lst[b].append(a)

MAX = 21e8
result_v = MAX
result_candidates = []

for i in range(1, N + 1):
    results = [MAX] * (N + 1)
    results[i] = 0

    q = []
    heapq.heappush(q, (0, i))

    while q:
        cost, via = heapq.heappop(q)

        if results[via] < cost:
            continue

        for nxt in lst[via]:
            if results[nxt] > cost + 1:
                results[nxt] = cost + 1
                heapq.heappush(q, (cost + 1, nxt))

    max_v = max(results[1:])
    if max_v < result_v:
        result_v = max_v
        result_candidates = [i]
    elif max_v == result_v:
        result_candidates.append(i)


print(result_v, len(result_candidates))
print(*result_candidates)