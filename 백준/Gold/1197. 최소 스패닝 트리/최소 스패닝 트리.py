import heapq


V, E = map(int, input().split())
q = []

for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

group = [x for x in range(V + 1)]


def find(a):
    while group[a] != a:
        a = group[a]
    return a


def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        if group_a < group_b:
            group[group_b] = group_a
        else:
            group[group_a] = group_b
        return 1


result = 0
while q:
    c, a, b = heapq.heappop(q)
    if union(a, b):
        result += c

print(result)