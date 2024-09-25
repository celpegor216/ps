N, Q = map(int, input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

results = [[21e8] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    results[i][i] = 0
    q = [(i, 21e8)]
    used = [0] * (N + 1)
    used[i] = 1
    while q:
        nq = []

        for now, cost in q:
            for nxt, nxt_cost in lst[now]:
                if used[nxt]:
                    continue

                used[nxt] = 1
                min_cost = min(cost, nxt_cost)
                results[i][nxt] = min_cost
                results[nxt][i] = min_cost
                nq.append((nxt, min_cost))

        q = nq

for _ in range(Q):
    K, V = map(int, input().split())

    result = 0
    for i in range(1, N + 1):
        if results[V][i] >= K:
            result += 1
    print(result)