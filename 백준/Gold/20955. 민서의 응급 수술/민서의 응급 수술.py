# 해답: https://yanoo.tistory.com/66

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
groups = list(range(N + 1))

def find(x):
    if groups[x] == x:
        return x
    groups[x] = find(groups[x])
    return groups[x]

def union(x, y):
    group_x, group_y = find(x), find(y)

    if group_x != group_y:
        groups[group_y] = group_x

total = 0
for m in range(M):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    
    # 연결하기 전 같은 그룹 == 사이클이므로 끊어야 함
    if find(x) == find(y):
        total += 1
    union(x, y)

for n in range(1, N):
    if find(n) != find(n + 1):
        total += 1
        union(n, n + 1)

print(total)