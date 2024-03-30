import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
q = []
total = 0

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
        return True
    return False

result = 0
while q:
    c, a, b = heapq.heappop(q)

    if union(a, b):
        result += c

flag = 0
standard = find(1)

for i in range(2, N + 1):
    if find(i) != standard:
        flag = 1
        break

if not flag:
    print(total - result)
else:
    print(-1)