import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

cut_order = [0] * M
for q in range(Q, 0, -1):
    cut_order[int(input()) - 1] = q
q = [(cut_order[m], m) for m in range(M)]
q.sort()

group = [n for n in range(N + 1)]
group_cnt = [1] * (N + 1)

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    res = 0
    if group_a != group_b:
        if group_a > group_b:
            group_a, group_b = group_b, group_a

        res = group_cnt[group_a] * group_cnt[group_b]

        group[group_b] = group_a
        group_cnt[group_a] += group_cnt[group_b]
        group_cnt[group_b] = 0

    return res

result = 0
for m in range(M):
    if not q[m][0]:
        union(*edges[q[m][1]])
    else:
        result += union(*edges[q[m][1]])

print(result)