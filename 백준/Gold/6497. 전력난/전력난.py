import heapq
import sys
input = sys.stdin.readline

while 1:
    N, M = map(int, input().split())

    if N == M == 0:
        break

    total = 0
    q = []

    for _ in range(M):
        a, b, c = map(int, input().split())
        heapq.heappush(q, (c, a, b))
        total += c

    group = [x for x in range(N + 1)]

    def find(a):
        if group[a] != a:
            group[a] = find(group[a])
        return group[a]

    def union(a, b):
        group_a, group_b = find(a), find(b)

        if group_a != group_b:
            if group_a < group_b:
                group[group_b] = group_a
            else:
                group[group_a] = group_b
            return 1
        return 0

    used = [0] * (N + 1)
    cnt = 0
    result = 0

    while q:
        c, a, b = heapq.heappop(q)

        res = union(a, b)

        if res:
            if not used[a]:
                used[a] = 1
                cnt += 1
            if not used[b]:
                used[b] = 1
                cnt += 1
            result += c
        
        if cnt == N:
            break

    print(total - result)