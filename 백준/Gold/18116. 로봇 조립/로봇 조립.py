import sys
input = sys.stdin.readline

N = int(input())

group = [x for x in range(1000001)]
cnt = [1] * 1000001

def find(a):
    if group[a] != a:
        group[a] = find(group[a])
    return group[a]

def union(a, b):
    group_a, group_b = find(a), find(b)

    if group_a != group_b:
        group[group_b] = group_a
        cnt[group_a] += cnt[group_b]
        cnt[group_b] = 0

for n in range(N):
    tmp = input().split()

    if tmp[0] == 'I':
        minv = int(tmp[1])
        maxv = int(tmp[2])

        if minv > maxv:
            minv, maxv = maxv, minv

        union(minv, maxv)
    else:
        g = find(int(tmp[1]))
        
        print(cnt[g])