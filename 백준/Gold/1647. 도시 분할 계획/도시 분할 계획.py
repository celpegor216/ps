import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[2])

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
maxv = 0

for a, b, c in lst:
    if union(a, b):
        result += c
        maxv = max(maxv, c)

print(result - maxv)