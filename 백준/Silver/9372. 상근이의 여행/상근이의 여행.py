import sys
input = sys.stdin.readline

T = int(input())

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

for _ in range(T):
    N, M = map(int, input().strip().split())

    group = [x for x in range(N + 1)]
    result = 0

    for _ in range(M):
        a, b = map(int, input().strip().split())
        result += union(a, b)
    
    print(result)