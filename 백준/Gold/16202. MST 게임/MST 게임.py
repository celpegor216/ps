import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

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

result = [0] * K
for k in range(K):
    group = [n for n in range(N + 1)]
    total = 0

    for m in range(k, M):
        a, b = edges[m]
        if union(a, b):
            total += m + 1
    
    standard = find(1)
    for n in range(2, N + 1):
        if find(n) != standard:
            standard = 0
            break
    
    if not standard:
        break
    else:
        result[k] = total

print(*result)