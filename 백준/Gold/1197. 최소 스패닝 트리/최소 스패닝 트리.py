import sys, heapq
input = sys.stdin.readline

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        if group_a > group_b:
            group_a, group_b = group_b, group_a
        group[group_b] = group_a
        return 1
    return 0

V, E = map(int, input().split())
group = [v for v in range(V + 1)]
q = []

for _ in range(E):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

result = 0
cnt = V - 1

while cnt:
    c, a, b = heapq.heappop(q)

    if union(a, b):
        result += c
        cnt -= 1

print(result)