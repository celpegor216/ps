import sys
input = sys.stdin.readline

def find(a, group):
    if group[a] != a:
        group[a] = find(group[a], group)
    return group[a]

def union(a, b, group, cnt):
    group_a, group_b = find(a, group), find(b, group)

    if group_a != group_b:
        group[group_b] = group_a
        cnt[group_a] += cnt[group_b]
        cnt[group_b] = 0

    return cnt[group_a]

T = int(input())

for t in range(T):
    F = int(input())

    idx = 1
    name_to_idx = dict()
    group = [x for x in range(200001)]
    cnt = [1] * 200001

    for f in range(F):
        a, b = input().split()
        
        if not name_to_idx.get(a):
            name_to_idx[a] = idx
            idx += 1
        
        if not name_to_idx.get(b):
            name_to_idx[b] = idx
            idx += 1
        
        print(union(name_to_idx[a], name_to_idx[b], group, cnt))
