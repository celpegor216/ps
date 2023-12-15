# 힌트: union find

N = int(input())
M = int(input())

group = [x for x in range(N)]

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a

for n in range(N):
    lst = list(map(int, input().split()))

    for i in range(N):
        if lst[i]:
            union(n, i)

path = list(map(int, input().split()))

flag = 'YES'

for m in range(M - 1):
    if find(path[m] - 1) != find(path[m + 1] - 1):
        flag = 'NO'
        break

print(flag)