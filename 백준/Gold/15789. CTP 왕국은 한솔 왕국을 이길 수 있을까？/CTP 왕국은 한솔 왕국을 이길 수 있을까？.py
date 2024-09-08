import sys
input = sys.stdin.readline

N, M = map(int, input().split())
groups = [n for n in range(N + 1)]
cnts = [1] * (N + 1)

def find(a):
    if groups[a] != a:
        groups[a] = find(groups[a])
    return groups[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        if group_a > group_b:
            group_a, group_b = group_b, group_a
        
        groups[group_b] = group_a
        cnts[group_a] += cnts[group_b]
        cnts[group_b] = 0

for _ in range(M):
    union(*map(int, input().split()))

A, B, K = map(int, input().split())
group_a = find(A)
group_b = find(B)

lefts = [cnts[x] for x in range(1, N + 1) if find(x) not in (group_a, group_b)]
print(sum(sorted(lefts, reverse=True)[:K]) + cnts[group_a])