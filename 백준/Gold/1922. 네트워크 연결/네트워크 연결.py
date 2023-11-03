import heapq

N = int(input())
M = int(input())
q = []

for m in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

groups = [x for x in range(N + 1)]

def find(a):
    if groups[a] != a:
        groups[a] = find(groups[a])
    return groups[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        groups[group_b] = group_a
        return True
    return False

result = 0
while q:
    c, a, b = heapq.heappop(q)

    if union(a, b):
        result += c

print(result)