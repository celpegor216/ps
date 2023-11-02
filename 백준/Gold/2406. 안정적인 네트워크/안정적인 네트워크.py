# 힌트: 최소 신장 트리
# 해답: https://velog.io/@j_aion/%EB%B0%B1%EC%A4%80-2406-%EC%95%88%EC%A0%95%EC%A0%81%EC%9D%B8-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC

import heapq

N, M = map(int, input().split())

group = [x for x in range(N + 1)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a == group_b:
        return False
    else:
        group[group_b] = group_a
        return True

for m in range(M):
    x, y = map(int, input().split())
    union(x, y)

q = []

for n in range(1, N + 1):
    cost = list(map(int, input().split()))

    if n == 1:
        continue

    for m in range(n + 1, N + 1):
        heapq.heappush(q, (cost[m - 1], n, m))

X = 0
connections = []
while q:
    cost, n, m = heapq.heappop(q)

    if union(n, m):
        X += cost
        connections.append((n, m))

print(X, len(connections))

for n, m in connections:
    print(n, m)